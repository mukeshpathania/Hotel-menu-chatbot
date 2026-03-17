from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)
order_cart = []
awaiting_location = False 
awaiting_phone = False

# Load menu
try:
    with open("menu.json") as f:
        menu = json.load(f)
except FileNotFoundError:
    print("Error: menu.json not found!")
    menu = {}

def show_menu():
    response = "📋 **Dhaba Menu Categories**\n"
    response += "Type a category name to see items:\n\n"
    for i, category in enumerate(menu, 1):
        display_name = category.replace('_', ' ').title()
        response += f"{i}. {display_name}\n"
    return response

def show_submenu(category, submenu):
    items = menu[category][submenu]
    display_sub = submenu.replace('_', ' ').title()
    response = f"📋 **{display_sub} Items**\n\n"
    for i, (item, price) in enumerate(items.items(), 1):
        response += f"{i}. {item} - ₹{price}\n"
    return response

def show_items_directly(category, items):
    display_cat = category.replace('_', ' ').title()
    response = f"📋 **{display_cat} Items**\n\n"
    for item, price in items.items():
        response += f"• {item} - ₹{price}\n"
    return response

def show_bill():
    if not order_cart:
        return "🛒 Your cart is empty."
    total = sum(item[1] for item in order_cart)
    response = "🧾 **Your Order**\n\n"
    for i, (item, price) in enumerate(order_cart, 1):
        response += f"{i}. {item} - ₹{price}\n"
    response += f"\n**Total = ₹{total}**\n\nType 'place order' to confirm."
    return response

def chatbot_response(message):
    global awaiting_location, order_cart 
    message = message.lower().strip()

    # 1. HANDLE LOCATION (MUST STAY AT TOP)
    if awaiting_location:
        awaiting_location = False  
        address = message
        order_cart.clear()  
        return f"✅ Order Confirmed!\n📍 Delivery to: {address}\n\nThank you for ordering from our Hotel! 🍽️"
    
    

    # 2. BASIC COMMANDS
    if message == "menu": return show_menu()
    if message == "bill": return show_bill()
    if message == "place order":
        if not order_cart: return "❌ Your cart is empty."
        awaiting_location = True 
        return "🚚 Great! Please type your **Delivery Address and Phone Number** to complete your order."

    # 3. SEARCH FOR SPECIFIC ITEMS (Priority Fix)
    # We look for the LONG name (Dal Makhani) first to avoid category confusion
    for category, content in menu.items():
        if isinstance(content, dict):
            for sub, items in content.items():
                # Case: Nested items (e.g., Dal -> Dal Makhani)
                if isinstance(items, dict): 
                    for item, price in items.items():
                        if item.lower() == message or item.lower() in message:
                            order_cart.append((item, price))
                            return f"🛒 {item} added to cart (₹{price})!\nType 'bill' to see your cart."
                
                # Case: Direct items (e.g., Breads -> Roti)
                elif isinstance(items, int): 
                    if sub.lower() == message or sub.lower() in message:
                        order_cart.append((sub, items))
                        return f"🛒 {sub} added to cart (₹{items})!\nType 'bill' to see your cart."

    # 4. CHECK CATEGORIES/SUBCATEGORIES (Only if no specific item was found)
    for category, content in menu.items():
        norm_cat = category.replace('_', ' ').lower()
        
        # We check for exact or near-exact category matches
        if norm_cat == message or (len(message) > 3 and norm_cat in message):
            if all(isinstance(v, int) for v in content.values()):
                return show_items_directly(category, content)
            
            options = "\n".join([f"• {s.replace('_',' ').title()}" for s in content.keys()])
            return f"Which {norm_cat.title()}?\n\n{options}\n\nType from the list above!"

        # Check Sub-categories (like 'Dal' or 'Paneer')
        if isinstance(content, dict):
            for sub in content:
                norm_sub = sub.replace('_', ' ').lower()
                if norm_sub == message or (len(message) > 3 and norm_sub in message):
                    return show_submenu(category, sub)

    return "❌ Item not found. Type 'menu' to see all categories."


@app.route('/')
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    response = chatbot_response(user_message)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
