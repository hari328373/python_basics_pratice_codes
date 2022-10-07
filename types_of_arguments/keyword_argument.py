# We can pass argument values by keyword i.e. by parameter name
def wish(name, msg):
    print("Hello", name, msg)


wish(name="john", msg="how are you")
wish(msg="how are you", name="john")
