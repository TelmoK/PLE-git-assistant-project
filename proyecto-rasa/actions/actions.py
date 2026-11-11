from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionGenerarComandoGit(Action):
    def name(self) -> Text:
        return "action_generar_comando_git"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Obtener la intención que gatilló esta acción
        intencion_actual = tracker.latest_message.get("intent", {}).get("name")
        
        comando_final = ""
        
        if intencion_actual == "inicializar_clonar":
            url = tracker.get_slot("url_repo")
            if url:
                comando_final = f"git clone {url}"
            else:
                comando_final = "git init"
                
        elif intencion_actual == "guardar_cambios":
            mensaje = tracker.get_slot("mensaje_commit")
            # Si el usuario no dio mensaje, le asignamos uno por defecto
            msg = mensaje if mensaje else "Update" 
            comando_final = f'git add . && git commit -m "{msg}"'
            
        elif intencion_actual == "crear_rama":
            rama = tracker.get_slot("nombre_rama")
            if rama:
                comando_final = f"git checkout -b {rama}"
            else:
                comando_final = "git checkout -b [nombre_de_rama_faltante]"
        
        # Enviar la respuesta de vuelta al usuario
        if comando_final:
            dispatcher.utter_message(text=comando_final)
        else:
            dispatcher.utter_message(text="No logré estructurar un comando para esa solicitud.")
            
        return []
