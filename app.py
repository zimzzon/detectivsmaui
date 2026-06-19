import streamlit as st
from PIL import Image

# --- KONFIGURATION & SETUP ---
APP_TITLE = "🕵️‍♂️ Detective Smaui: Die Fallakte der Faultiere"

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
                "text": "Sehr gut Detective, das konnte nur ein geschultes Auge erkennen. Wahrscheinlich träumt Mr. Fauls von seiner Weltreise damals. Schließlich hat er dort auch Fauline kennengelernt. Wo warst Du eigentlich damals?",
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
        "story": """Kaum ist das Rätsel um das Spiel gelöst, herrscht schon wieder helle Aufregung am Strand. Plötzlich kommt Miguel völlig außer Atem angelaufen. Er ist extrem nervös, fuchtelt mit den Armen und fängt sofort an, wie ein Wasserfall auf dich – **Detective Smaui** – einzureden. 

Er wollte eigentlich gerade ein großes Match mit Bollecks Geschwistern starten, doch der Schock sitzt tief: **Die Zwillinge sind spurlos verschwunden!** Niemand hat sie in den Dünen gesehen und der sportliche Strandtag droht ins Wasser zu fallen. Und wir alle wissen: Ohne die beiden fehlt einfach die wichtigste Bolleckaction!

Miguel blickt dich mit flehenden Augen an: **„Bitte hilf mir, die Zwillinge zu finden, Schmiegi braucht dich jetzt, Detective Smaui!“** 

*Du rückst deine Deerstalker-Mütze zurecht, nimmst die Lupe in die Pfote und scannst den heißen Sand nach den ersten Spuren ab. Dein detektivischer Instinkt sagt dir, dass die Zwillinge einen Hinweis hinterlassen haben müssen...*""",
        "questions": [
            {
                "type": "code",
                "text": "Irgendwo in den Bildern muss sich ein Hinweis verstecken. Welchen Urlaub mag Schmiegi am liebsten? Finde alle passenden Fotos und bilde mit den Buchstaben auf den Rückseiten den Namen der schnellsten Skipuppe.",
                "hint": "Pisten.......!",
                "correct_answer": "CARLOS"
            },
            {
                "type": "code",
                "text": "Das hat also schonmal als Code gestimmt, wahrscheinlich müssen wir weiter in den Bergen suchen. Auf welchem Bild hast du das größte Abenteuer einer Smaui erlebt?",
                "hint": "Schmetterlinge, Schneefelder und ein sehr kleines Bett, aber immer dabei: das Glätteisen!",
                "correct_answer": "GPFL"
            },
            {
                "type": "multiple-choice",
                "text": "Wir kommen dem ganzen immer Näher, doch Miggi wird auch immer ungehaltener - so kennen wir ihn. Die nächste Frage bezieht sich auf ein Bild mit dem Code (auf der Rückseite) STBB. Wo wurde dieses Bild aufgenommen?",
                "options": ["Lofer", "Alpendorf", "Paguera"],
                "hint": "Ist das nicht das Steinbergbad?",
                "correct_answer": "Lofer"
            },
            {
                "type": "code",
                "text": "Plötzlich hat Fauline eine Idee, vielleicht ist der nächste Hinweis auf einem Gipfelfoto versteckt, aber nicht deinem Gipfelfoto...welches Bild könnte es sein?",
                "hint": "Hier kommt der Kleine ganz groß raus!",
                "correct_answer": "FLNH"
            },
            {
                "type": "code",
                "text": "Absolut richtig! Mann war das ein Abenteuer für den kleinen Racker. Plötzlich wacht Mr. Fauls auf. Nachdem Detective Smaui ihn auf den neuesten Stand gebracht hat, hat Mr. Fauls eine geniale und doch so simple Idee: Habt Ihr schon bei Bolleck geschaut ob seine Schwestern dort sind? Eventuell steht dort auch der nächste Code.",
                "hint": "Klopf-klopf!",
                "correct_answer": "BLLK"
            }
        ],
        "reward_text": "🎉 Fall 2 gelöst! Unglaublich, Detective Smaui! Die Zwillinge sind wieder da und Schmiegi kann endlich die Bolleckaction starten. Als Dankeschön für deinen messerscharfen Verstand darfst du dir jetzt Geschenk Nummer 2 nehmen! 🎁"
    },
    {
        "fall_name": "Fall 3: Wer hat Juie gesehen?",
        "story": """Nachdem die Faultiere zuerst das heißersehnte Spiel und anschließend mit deiner meisterhaften Hilfe auch Bollecks Schwestern unversehrt wiedergefunden haben, kehrt am Strand langsam wieder Ruhe ein. Die Erleichterung ist groß, Miguel atmet auf und Mr. Fauls reibt sich veträumt seine Äuglein. 

Doch als du deinen Blick schweifen lässt, schlägt dein detektivischer Instinkt plötzlich Alarm. Das Trüffelschwein spürt es sofort: Die Harmonie trügt. Irgendwer oder irgendetwas fehlt hier doch in der Runde... 

Ein kurzer Kontrollblick durch die Lupe bestätigt den schrecklichen Verdacht. Jemand hat die allgemeine Verwirrung genutzt und sich klammheimlich aus dem Staub gemacht! 

**Detective Smaui, die Ermittlung läuft wieder! Wer fehlt am Strand?**""",
        "questions": [
            {
                "type": "multiple-choice",
                "text": "Wer hat sich still und leise aus dem Staub gemacht und die Mäuseschaft in helle Aufregung versetzt?",
                "options": ["Juie", "Momo", "Kraki"],
                "hint": "Er hat große Ohren, liebt intergalaktische Abenteuer und wird von allen schmerzlich vermisst!",
                "correct_answer": "Juie"
            },
	{
                "type": "code",
                "text": "Potzblitz! Wie konnte sich Juie denn aus dem Staub machen....um Ihn am Starnd zu suchen brauchen wir ein Bild auf dem er aleine gut zu erkennen ist. ",
                "hint": "Am besten ein Foto wo er alleine drauf ist!",
                "correct_answer": "4LFR"
            },
{
                "type": "code",
                "text": "Eine sehr gute Bildauswahl. Mein Gott ist Juie süß! Aber zur Sicherheit sollten wir die anderen Bilder auch mitnehmen zur Suche. Trage als Code alle Zahlen von klein nach groß ein. ",
                "hint": "Pro Bild eine Zahl. Zusammen dann 5 Zahlen!",
                "correct_answer": "12447"
            },
{
                "type": "code",
                "text": "Ok, die ersten Hinweise der anderen Badegäste lassen darau schließen, dass Juie sich absichtlich versteckt. Ob er mit Schmiegi etwas Schabernack treibt? Wir sollten Schmiegi nochmal genauer Fragen. Gebe den Code MIGI ein. ",
                "hint": "Pro Bild eine Zahl. Zusammen dann 5 Zahlen!",
                "correct_answer": "MIGI"
            },
{
                "type": "code",
                "text": "Migi schaut schon ganz verschmitzt als Du dich in seine Richtung aufmachst. Es hätte dir vorher schon auffallen können, dass Migi auffallen gelassen war. das passt ja eigentlich nicht so wirklich zu Ihm wie wir bei Bollecks Schwestern erfahren haben. Du fragst Migi, ob er weiß wo Juie ist, aber das einzige was Migi macht ist ein Dach mit seinen Händen. Was kann das nur bedeuten? Trage den Code auf der Rückseite ein. ",
                "hint": "Der Berg ruft!",
                "correct_answer": "DBGR"
            },

{
                "type": "code",
                "text": "Migi ist beeindruckt wie schnell Du die Rätsel löst. Aber bevor er Dir den letzten Hinweis gibt, hat er noch folgende Fragen für Dich: \n 1. Auf wie vielen Bildern ist ein Smartphone zu sehen? \n 2. Auf einem Bild ist etwas zu Essen zu sehen. An welche Zahl erinnert das Bild? \n 3. Auf wie vielen Bildern bin ich zu sehen? \n 4. Auf wie vielen Bildern sind Hasen zu sehen (bzw Teile erkennbar)? ",
                "hint": "Jede Lösung (Zahl) hintereinader geschrieben ergibt den fünfstelligen Code!",
                "correct_answer": "38610"
            },

{
                "type": "code",
                "text": "Migi gibt sich geschlagen. Gegen Detective Smaui hat er keine Chance. Als letzten Hinweis übergibt Dir Miguel ein kleines Geschenk. Trage den Code auf dem Zettel im Geschenk als letzten Code ein.",
                "hint": "Ganz dolle!",
                "correct_answer": "LOVE"
            }


        ],
	
        "reward_text": "🏆 🎉 MEISTERDETEKTIVIN! Du hast alle drei Fälle gelöst. Detective Smaui (aka das Trüffelschwein) hat wieder einmal zugeschlagen. Juie erwartet Dich auf dem Sofa...! 🎁"
    }
]

# --- SESSION STATE INITIALISIERUNG ---
if "is_smaui" not in st.session_state:
    st.session_state.is_smaui = False
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

# SCHRITT 0: DER IDENTITÄTS-CHECK
if not st.session_state.is_smaui:
    st.subheader("🔒 Streng geheim – Zutrittskontrolle")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(smaui_image, caption="Identität wird geprüft...", use_column_width=True)
    with col2:
        st.write("""
        Halt! Diese Ermittlungsakten enthalten hochbrisante Informationen über die Faultiere, 
        geheime Codes und intergalaktische Mäuse-Verschwörungen.
        
        Der Zugriff ist ausschließlich der Chef-Ermittlerin Detective Smaui gestattet.
        """)
        
        # Ein schöner Bestätigungsknopf
        if st.button("Ich bestätige, dass ich Detective Smaui bist! 🕵️‍♂️✨", type="primary"):
            st.session_state.is_smaui = True
            st.rerun()

# WENN CKECH BESTANDEN: DAS EIGENTLICHE SPIEL STARTET
else:
    # SPIEL KOMPLETT VORBEI
    if st.session_state.game_completed:
        st.balloons()
        st.image(smaui_image, caption="Detective Smaui hat alle Fälle abgeschlossen!", use_column_width=True)
        st.success(FAELLE[-1]["reward_text"])
        if st.button("Das Abenteuer neustarten"):
            st.session_state.is_smaui = False
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