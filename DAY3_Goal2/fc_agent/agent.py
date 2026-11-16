import os
import sys
from google import genai
from google.genai import types

from tools import get_order, get_shipping, check_refund_policy, escalate_to_human

def run_customer_agent(user_query: str):
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not set!")
        return
    
    client = genai.Client(api_key=api_key)
    
    my_tools = [get_order, get_shipping, check_refund_policy, escalate_to_human]
    tool_map = {
        "get_order": get_order,
        "get_shipping": get_shipping,
        "check_refund_policy": check_refund_policy,
        "escalate_to_human": escalate_to_human
    }

    system_instruction = (
        "You are an expert, polite, and efficient AI customer service assistant for an e-commerce platform. "
        "You have access to tools to lookup orders, check shipping status, check refund/return policies, and escalate to human supervisors. "
        "ALWAYS use the appropriate tools when answering customer inquiries about orders or policies. "
        "CRITICAL ESCALATION RULE: If a customer is angry, uses aggressive language, reports damaged/undelivered disputed items, "
        "or asks explicitly for a human manager, you MUST call the `escalate_to_human` tool immediately with a clear reason."
    )

    print(f"\n[Customer Query]: {user_query}")
    print("-" * 50)

    try:
        chat = client.chats.create(
            model="gemini-3.8-flash",
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                tools=my_tools,
                temperature=0.0
            )
        )

        response = chat.send_message(user_query)

        while response.function_calls:
            for function_call in response.function_calls:
                fn_name = function_call.name
                fn_args = function_call.args
                print(f"-> [Agent Tool Call Requested]: {fn_name} with args {fn_args}")

                if fn_name in tool_map:
                    tool_result = tool_map[fn_name](**fn_args)
                    print(f"<- [Tool Result Executed]: {tool_result}")

                    response = chat.send_message(
                        types.Part.from_function_response(
                            name=fn_name,
                            response={"result": tool_result}
                        )
                    )
                else:
                    print(f"Error: Unknown tool '{fn_name}' requested.")
                    break

        print("-" * 50)
        print(f"[Agent Final Response]:\n{response.text}\n")
        return response.text

    except Exception as e:
        print(f"\n[API Execution Error]: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
    else:
        query = "What is the status of order ORD-102 and what is its shipping detail?"
    
    run_customer_agent(query)

