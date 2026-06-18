import streamlit as st
from PIL import Image

# --- KONFIGURATION & SETUP ---
APP_TITLE = "🕵️‍♂️ Detective Smaui: Die drei Geschenke-Fälle"

# --- KONFIGURATION & SETUP ---
APP_TITLE = "🕵️‍♂️ Detective Smaui: Die drei Geschenke-Fälle"

# Lade das Hauptbild von Detective Smaui (detective-smaui-foto.png)
try:
    smaui_image = Image.open('detective-smaui-foto.png')
except FileNotFoundError:
    st.error("Fehler: Die Datei 'detective-smaui-foto.png' wurde nicht gefunden. Bitte lade sie im gleichen Ordner hoch!")
    st.stop()

# --- DIE DREI ERMITTLUNGSAKTEN (FRAGEN & CODES) ---
# Hier kannst du jetzt für jeden Fall die echten Fragen, Typen und Antworten eintragen!
FAELLE = [
    {
        "fall_name": "Fall 1: Das Geheimnis des Origami-Pingu",
        "story": "Ein extrem gemütliches Faultier hat sich am Strand zusammengerollt und weigert sich, aufzustehen. Es murmelt ständig etwas von einem papiernen Pinguin... Wir müssen das Rätsel um das Spiel 'Sea Salt & Paper' lösen!",
        "questions": [
            {
                "type": "code",
                "text": "Detective Smaui braucht den ersten Hinweis: Welches der ausgedruckten Fotos zeigt das Faultier in seiner natürlichen, absolut tiefentspannten Umgebung? Findet das Bild und gebt den Code von der Rückseite ein!",
                "hint": "Hinweis von Smaui: Sucht nach dem Bild, auf dem man vor lauter Gemütlichkeit fast selbst einschläft.",
                "correct_answer": "PINGU01"
            },
            {
                "type": "multiple-choice",
                "text": "Bevor uns das Faultier den Weg zum ersten Geschenk zeigt, ein kleiner Test: Wie viele Sekunden kann ein Faultier schätzungsweise die Luft anhalten (länger als ein Delfin!)?",
                "options": ["Etwa 10 Minuten", "Bis zu 40 Minuten", "Gar nicht, es vergisst es einfach"],
                "hint": "Smauis Tipp: Sie sind langsamer, aber unter Wasser wahre Meister!",
                "correct_answer": "Bis zu 40 Minuten"
            }
        ],
        "reward_text": "🎉 Fall 1 gelöst! Das Faultier pennt weiter, aber es hat euch das erste Geschenk hinterlassen: Das Spiel **Sea Salt & Paper**! (Hier kannst du das echte Geschenk überreichen!)"
    },
    {
        "fall_name": "Fall 2: Wo sind Bollecks Geschwister?",
        "story": "Es ist Zeit für die große Bolleckaction am Strand! Doch Schock schwere Not: Die Faultier-Geschwisterbande hat sich im Dünensand aus den Augen verloren. Detective Smaui muss die Familienzusammenführung koordinieren.",
        "questions": [
            {
                "type": "code",
                "text": "Sucht das ausgedruckte Bild, das die legendärste Beachaction oder Bolleckaction eurer bisherigen Reisen zeigt. Welcher Code steht hinten drauf?",
                "hint": "Smauis Tipp: Sand, Sonne und jede Menge Action sind hier zu sehen!",
                "correct_answer": "BEACH99"
            }
        ],
        "reward_text": "🎉 Fall 2 gelöst! Die Geschwister sind wieder vereint und bereit für die nächste Bolleckaction! Zeit für Geschenk Nummer 2!"
    },
    {
        "fall_name": "Fall 3: Wer hat Juie gesehen?",
        "story": "Das große Finale! Der kleine Baby Yoda – bei uns nur bekannt als Juie – ist spurlos verschwunden. Gerüchten zufolge hat er sich unter die Mäuseschaft gemischt, um Detective Smaui zu besuchen. Wir müssen ihn finden, um das finale Geheimnis zu lüften!",
        "questions": [
            {
                "type": "multiple-choice",
                "text": "Juie hat eine Nachricht in intergalaktischer Mäusesprache hinterlassen. Was ist seine absolute Lieblingsspeise, wenn er nicht gerade die Macht benutzt?",
                "options": ["Blaukekse", "Käsehäppchen", "Krabben-Suppe"],
                "hint": "Smauis Tipp: In einer bestimmten Folge klaut er sie einem anderen Kind...",
                "correct_answer": "Blaukekse"
            },
            {
                "type": "code",
                "text": "Das letzte Rätsel! Findet das Bild, auf dem die ganze Mäuseschaft (oder eure beste gemeinsame Erinnerung) versammelt ist. Das ist der Weg zum Hauptgeschenk!",
                "hint": "Der allerletzte Code trennt euch vom Schatz. Schaut ganz genau hin!",
                "correct_answer": "JUICESTART"
            }
        ],
        "reward_text": "🏆 🎉 MEISTERDETEKTIVE! Ihr habt Juie gefunden und alle drei Fälle gelöst. Detective Smaui zieht seinen Hut vor euch. Hier ist euer wohlverdientes Hauptgeschenk! 🎁"
    }
]

# --- SESSION STATE INITIALISIERUNG ---
if "current_fall" not in st.session_state:
    st.session_state.current_fall = 0
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "fall_completed" not in st.session_state:
    st.session_state.fall_completed = False
if "game_completed" not in st.session_state:
    st.session_state.game_completed = False

# --- UI LOGIK ---
st.title(APP_TITLE)
st.write("---")

# SPIEL KOMPLETT VORBEI
if st.session_state.game_completed:
    st.balloons()
    st.image(smaui_image, caption="Detective Smaui hat den Fall abgeschlossen!", use_column_width=True)
    st.success(FAELLE[-1]["reward_text"])
    if st.button("Das Abenteuer neustarten"):
        st.session_state.current_fall = 0
        st.session_state.current_question = 0
        st.session_state.fall_completed = False
        st.session_state.game_completed = False
        st.rerun()

# EIN FALL WURDE GERADE GELÖST
elif st.session_state.fall_completed:
    st.balloons()
    aktueller_fall = FAELLE[st.session_state.current_fall]
    st.success(aktueller_fall["reward_text"])
    
    if st.button("Nächsten Fall in der Akte öffnen 📂", type="primary"):
        st.session_state.current_fall += 1
        st.session_state.current_question = 0
        st.session_state.fall_completed = False
        st.rerun()

# REGULÄRER SPIELABLAUF
else:
    fall_idx = st.session_state.current_fall
    frag_idx = st.session_state.current_question
    
    aktueller_fall = FAELLE[fall_idx]
    aktuelle_frage = aktueller_fall["questions"][frag_idx]
    
    # Fortschrittsanzeige über alle Fälle hinweg
    st.subheader(aktueller_fall["fall_name"])
    st.caption(f"Frage {frag_idx + 1} von {len(aktueller_fall['questions'])} in diesem Fall")
    
    # Layout: Smauis Bild links, Rätsel rechts
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image(smaui_image, caption="Detective Smaui ermittelt...", use_column_width=True)
        
    with col2:
        if frag_idx == 0:
            st.info(aktueller_fall["story"])
        
        st.markdown(f"**Ermittlungsschritt:** {aktuelle_frage['text']}")
        
        with st.expander("💡 Lupe herausholen (Hinweis)"):
            st.write(aktuelle_frage["hint"])
            
        # Eingabe-Logik je nach Typ
        user_submission = None
        
        if aktuelle_frage["type"] == "code":
            user_input = st.text_input("Code eingeben:", key=f"code_{fall_idx}_{frag_idx}").strip()
            if st.button("Code prüfen 🔑", type="primary"):
                user_submission = user_input
        
        elif aktuelle_frage["type"] == "multiple-choice":
            choice = st.radio("Antwort auswählen:", ["Bitte auswählen..."] + aktuelle_frage["options"], key=f"radio_{fall_idx}_{frag_idx}")
            if st.button("Antwort einloggen 📝", type="primary") and choice != "Bitte auswählen...":
                user_submission = choice
                
        # Auswertung
        if user_submission is not None:
            is_correct = False
            if aktuelle_frage["type"] == "code":
                is_correct = user_submission.lower() == aktuelle_frage["correct_answer"].lower()
            else:
                is_correct = user_submission == aktuelle_frage["correct_answer"]
                
            if is_correct:
                st.success("🕵️‍♂️ Smaui sagt: Kombiniert wie ein Meister! Richtig!")
                
                # Prüfen, ob es noch mehr Fragen im aktuellen Fall gibt
                if frag_idx + 1 < len(aktueller_fall["questions"]):
                    st.session_state.current_question += 1
                else:
                    # Fall ist geschafft!
                    if fall_idx + 1 < len(FAELLE):
                        st.session_state.fall_completed = True
                    else:
                        st.session_state.game_completed = True
                st.rerun()
            else:
                st.error("❌ Das war leider falsch. Detective Smaui schüttelt den Kopf. Sucht weiter!")