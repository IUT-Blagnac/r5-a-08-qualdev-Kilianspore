from behave import given, when, then
import tkinter as tk
from compteur import StartPage

@given("l'application est lancée")
def step_given_application_launched(context):
    context.app = StartPage()
    context.app.update()

@when('je clique sur "{button_text}"')
def step_when_click_button(context, button_text):
    for child in context.app.winfo_children():
        if isinstance(child, tk.Button) and child.cget("text") == button_text:
            child.invoke()  # Simule un clic
            context.app.update()
            return
    raise Exception(f"Bouton {button_text} non trouvé")

@when('je saisis "{value}" dans "{label_text}"')
def step_when_enter_value_in_field(context, value, label_text):
    for child in context.app.winfo_children():
        if isinstance(child, tk.Label) and child.cget("text") == label_text:
            entry_index = context.app.winfo_children().index(child) + 1
            entry = context.app.winfo_children()[entry_index]
            if isinstance(entry, tk.Entry):
                entry.delete(0, tk.END)  # Effacer le champ
                entry.insert(0, value)   # Insérer la valeur (même vide)
                context.app.update()
                return
    raise Exception(f"Champ pour {label_text} non trouvé")


@then('le compteur doit afficher "{expected_text}"')
def step_then_verify_counter(context, expected_text):
    label_text = context.app.label.cget("text")
    assert label_text == expected_text, f"Attendu: {expected_text}, obtenu: {label_text}"
