import streamlit as st
from PIL import Image

# --- KONFIGURATION & SETUP ---
APP_TITLE = "🕵️‍♂️ Detective Smaui: Die drei Geschenke-Fälle"

# Lade das Hauptbild von Detective Smaui (detective-smaui-foto.png)
try:
    smaui_image = Image.open('detective-smaui-foto.png')
except FileNotFoundError:
    st.error("Fehler: Die Datei 'detective-smaui-foto.png' wurde nicht gefunden. Bitte lade sie im gleichen Ordner hoch!")
    st.stop()

# --- DIE DREI ERMITTLUNGSAKTEN (FRAGEN & CODES) ---
FAELLE = [
    {
        "fall_name": "Fall 1: Das Geheimnis des Origami-Pingu",
        "story": """Die Sonne brennt heiß vom Himmel, der Sand ist perfekt gewärmt – eigentlich die absoluten Traumkonditionen für einen tiefentspannten Tag am Strand. Genau das hatten sich die Faultiere auch fest vorgenommen: exzessives, professionelles Faulenzen in der Sonne. 

Damit zwischen den Nickerchen keine Langeweile aufkommt, hatte Mr. Fauls versprochen, ein ganz besonderes Spiel einzupacken. Doch als Fauline und Coco die Strandtasche durchwühlen, bricht leichte Panik aus: **Das Spiel ist unauffindbar!** Wo im Dünensand hat er es bloß versteckt?

Eine Nachfrage beim Meister des Tiefschlafs bringt absolut gar nichts. Mr. Fauls ist augenblicklich im Land der Träume versunken, völlig weggetreten und absolut nicht mehr ansprechbar – typisch Mr. Fauls eben! Das Einzige, was er im Schlaf leise und kryptisch vor sich hin murmelt, klingt wie: *„...Papier... Pinguin...“*

Fauline und Coco stehen vor einem Rätsel. Papier? Pinguin? Das macht im heißen Sand doch überhaupt keinen Sinn! In ihrer Verzweiflung bleibt den beiden nur noch eine Hoffnung: **Detective Smaui!** 

Unter den Faultieren genießt du schließlich nicht ohne Grund den ehrfurchtssvollen Spitznamen *„Das Trüffelschwein“* – denn deinem messerscharfen Verstand und deiner legendären Spürnase bleibt absolut nichts verborgen. 

Fauline und Coco blicken dich mit großen, bittenden Faultieraugen an: 
**„Detective Smaui, bitte hilf uns! Du musst dieses Rätsel für uns lösen! Schau dir die Beweisfotos an, die vor dir liegen...“**""",
        "questions": [
            {
                "type": "code",
                "text": "Fauline reicht dir die Lupe: 'Haben wir nicht ein Foto wo Mr. Fauls schonmal so tief im Schlummerland war? Finde das Bild, dreh es um und gib den Code ein!'",
                "hint": "Ich glaube das war ein Faultiersalat.",
                "correct_answer": "PNGN"
            },
            {
                "type": "multiple-choice",
                "text": "Wahrscheinlich träumt Mr. Fauls von seiner Weltreise damals. Schließlich hat er dort auch Fauline kennengelernt. Wo warst Du eigentlich damals?",
                "options": ["Lofer", "Mallorca", "Köln"],
                "hint": "Viva Espana!",
                "correct_answer": "Mallorca"
            },
            {
                "type": "multiple-choice",
                "text": "Mhh... so wirklich bringt Euch das nicht weiter. Manchmal erzählt Mr. Fauls Fauline und Faulinho auch von seiner Zeit bevor er Fauline kennengelernt hat. Wie war nochmal die Bewegung die dafür gesorgt hat, dass Mr. Fauls so richtig aufgeblüht ist?",
                "options": ["#wakeupmrfauls", "#FauliForPresident", "#freemrfauls"],
                "hint": "Wer hier einen Hinweis braucht...",
                "correct_answer": "#freemrfauls"
            },
            {
                "type": "code",
                "text": "Fauline hat einen Geistesblitz, #freemrfauls das ist es! Wahrscheinlich hat Mr. Fauls dort das Spiel versteckt! Gib die Lösung als Code ein.",
                "hint": "Andere schlafen drauf, Mr. Fauls darunter.",
                "correct_answer": "Kissen"
            }
        ],
        "reward_text": "🎉 Unglaublich! Detective Smaui hat messerscharf kombiniert! Fauline und Coco tanzen vor Freude. Mr. Fauls pennt zwar weiter, aber deine Spürnase hat das Versteck enttarnt: Das erste Geschenk wurde erfolgreich von dir aufgespürt! 🎁"
    },
    {
        "fall_name": "Fall 2: Wo sind Bollecks Geschwister?",
        "story": "Die Ermittlung geht weiter, Detective Smaui! Kaum ist das erste Rätsel gelöst, wartet schon das nächste Abenteuer bei der Beachaction...",
        "questions": [
            {
                "type": "code",
                "text": "Sucht das ausgedruckte Bild, das die legendärste Beachaction oder Bolleckaction eurer bisherigen Reisen zeigt. Welcher Code steht hinten drauf?",
                "hint": "Hier kommt bald dein echter Hinweis hin!",
                "correct_answer": "BEACH99"
            }
        ],
        "reward_text": "🎉 Fall 2 gelöst! Die Geschwister sind wieder vereint und bereit für die nächste Bolleckaction! Zeit für Geschenk Nummer 2! 🎁"
    },
    {
        "fall_name": "Fall 3: Wer hat Juie gesehen?",
        "story": "Das große Finale für Detective Smaui! Der kleine Baby Yoda (Juie) hat sich unter die Mäuseschaft gemischt. Finden wir ihn!",
        "questions": [
            {
                "type": "code",
                "text": "Findet das finale Bild für das Hauptgeschenk. Welcher Code versteckt sich hier?",
                "hint": "Der allerletzte Code trennt dich vom Schatz.",
                "correct_answer": "FINALE"
            }
        ],
        "reward_text": "🏆 🎉 MEISTERDETEKTIVIN! Du hast alle drei Fälle gelöst. Detective Smaui (aka das Trüffelschwein) hat wieder einmal zugeschlagen. Hier ist dein wohlverdientes Hauptgeschenk! 🎁"
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
    st.image(smaui_image, caption="Detective Smaui hat alle Fälle abgeschlossen!", use_column_width=True)
    st.success(FAELLE[-1]["reward_text"])
    if st.button("Das Abenteuer neustarten"):
        st.session_state.current_fall = 0
        st.session_state.current_question = 0
        st.session_state.fall_completed = False
        st.session_state.game_completed = False
        st.rerun()

# EIN FALL WURDE GERADE GELÖST (Hier schaltet die App nach Fall 1 weiter!)
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
    
    st.subheader(aktueller_fall["fall_name"])
    st.caption(f"Frage {frag_idx + 1} von {len(aktueller_fall['questions'])} in diesem Fall")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image(smaui_image, caption="Detective Smauis Ermittlungsakte", use_column_width=True)
        
    with col2:
        if frag_idx == 0:
            st.info(aktueller_fall["story"])
        
        st.markdown(f"**Ermittlungsschritt:** {aktuelle_frage['text']}")
        
        with st.expander("💡 Lupe herausholen (Hinweis)"):
            st.write(aktuelle_frage["hint"])
            
        user_submission = None
        
        if aktuelle_frage["type"] == "code":
            user_input = st.text_input("Code eingeben:", key=f"code_{fall_idx}_{frag_idx}").strip()
            if st.button("Code prüfen 🔑", type="primary"):
                user_submission = user_input
        
        elif aktuelle_frage["type"] == "multiple-choice":
            choice = st.radio("Antwort auswählen:", ["Bitte auswählen..."] + aktuelle_frage["options"], key=f"radio_{fall_idx}_{frag_idx}")
            if st.button("Antwort einloggen 📝", type="primary") and choice != "Bitte auswählen...":
                user_submission = choice
                
        if user_submission is not None:
            is_correct = False
            if aktuelle_frage["type"] == "code":
                is_correct = user_submission.lower() == aktuelle_frage["correct_answer"].lower()
            else:
                is_correct = user_submission == aktuelle_frage["correct_answer"]
                
            if is_correct:
                st.success("🕵️‍♂️ Hervorragend kombiniert, Detective Smaui! Das ist richtig!")
                
                if frag_idx + 1 < len(aktueller_fall["questions"]):
                    st.session_state.current_question += 1
                else:
                    if fall_idx + 1 < len(FAELLE):
                        st.session_state.fall_completed = True
                    else:
                        st.session_state.game_completed = True
                st.rerun()
            else:
                st.error("❌ Das war leider falsch. Detective Smaui, schau dir die Beweise lieber noch einmal an!")