form_values = {
    "start-input": ""
}

def submit_handler(event = None):
    if event:
        event.preventDefault()
        x = form_values['start-input']
        display(f"{x}", target="form-values")

def reset_handler(event = None):
    if event:
        form_values = {
            "start-input": ""
        }


def start_input_handler(event = None):
    if event:
        form_values["start-input"] = event.target.value


Element("start-input").element.oninput = start_input_handler
Element("form").element.onsubmit = submit_handler
Element("form").element.onreset = reset_handler