import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "fake_orders.json")

def _load_db():
    if not os.path.exists(DB_PATH):
        return []
    with open(DB_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def get_order(order_id: str) -> dict:
    """Get full order details including customer name, item, amount, order date, and status for a given order_id."""
    orders = _load_db()
    for order in orders:
        if order["order_id"].upper() == order_id.upper():
            return order
    return {"error": f"Order ID '{order_id}' not found in database."}

def get_shipping(order_id: str) -> dict:
    """Get real-time shipping status and tracking details for a given order_id."""
    orders = _load_db()
    for order in orders:
        if order["order_id"].upper() == order_id.upper():
            return {
                "order_id": order["order_id"],
                "shipping_status": order.get("shipping_status"),
                "tracking_id": order.get("tracking_id"),
                "status": order.get("status")
            }
    return {"error": f"Order ID '{order_id}' not found for shipping lookup."}

def check_refund_policy(category: str) -> dict:
    """Check the refund and return policy rules based on the product category (e.g. electronics, apparel, groceries, footwear)."""
    policies = {
        "electronics": "7-day return window from delivery date. Item must be in original packaging with all accessories. 10% restocking fee applies if opened unless defective.",
        "apparel": "15-day return or exchange window. Tags must be intact and unwashed.",
        "groceries": "Non-returnable unless received damaged or expired. Claim must be raised within 24 hours.",
        "footwear": "10-day return/exchange window for unworn items in original box.",
        "home_kitchen": "7-day return window. Damaged or missing parts must be reported within 48 hours.",
        "beauty": "Non-returnable due to hygiene reasons unless sealed product is damaged upon delivery."
    }
    cat = category.lower().strip()
    policy = policies.get(cat, "Standard 7-day return policy applies to all general merchandise in original condition.")
    return {"category": cat, "policy_details": policy}

def escalate_to_human(reason: str) -> dict:
    """Escalate the customer query to a human customer support agent when the issue involves disputes, angry customers, or complex system errors."""
    return {
        "status": "escalated",
        "message": "Your issue has been successfully escalated to a senior support supervisor.",
        "reason_logged": reason,
        "estimated_callback": "Within 2 to 4 business hours"
    }
