
import speech_recognition  # распознавание пользовательской речи (Speech-To-Text)
import pyttsx3  # синтез речи (Text-To-Speech)
import wave  # создание и чтение аудиофайлов формата wav
import os  # работа с файловой системой


class VoiceAssistant:
    """
    Настройки голосового ассистента, включающие имя, пол, язык речи
    """
    name = ""
    sex = ""
    speech_language = ""
    recognition_language = ""


def setup_assistant_voice():
    """
    Установка голоса по умолчанию (индекс может меняться в 
    зависимости от настроек операционной системы)
    """
    voices = ttsEngine.getProperty("voices")

    if assistant.speech_language == "en":
        assistant.recognition_language = "en-US"
        if assistant.sex == "male":
            # Microsoft Zira Desktop - English (United States)
            ttsEngine.setProperty("voice", voices[0].id)
        else:
            # Microsoft David Desktop - English (United States)
            ttsEngine.setProperty("voice", voices[1].id)
    else:
        assistant.recognition_language = "ru-RU"
        # Microsoft Irina Desktop - Russian
        ttsEngine.setProperty("voice", voices[0].id)


def play_voice_assistant_speech(text_to_speech):
    
    # Проигрывание речи ответов голосового ассистента (без сохранения аудио)
    # :param text_to_speech: текст, который нужно преобразовать в речь
    
    ttsEngine.say(str(text_to_speech))
    ttsEngine.runAndWait()


def record_and_recognize_audio(*args: tuple):
    """
    Запись и распознавание аудио
    """
    with microphone:
        recognized_data = ""

        # регулирование уровня окружающего шума
        recognizer.adjust_for_ambient_noise(microphone, duration=2)

        try:
            print("Listening...")
            audio = recognizer.listen(microphone, 5, 5)

            with open("microphone-results.wav", "wb") as file:
                file.write(audio.get_wav_data())

        except speech_recognition.WaitTimeoutError:
            print("Can you check if your microphone is on, please?")
            return

        # использование online-распознавания через Google 
        # (высокое качество распознавания)
        try:
            print("Started recognition...")
            recognized_data = recognizer.recognize_google(audio, language="ru").lower()

        except speech_recognition.UnknownValueError:
            pass


        return recognized_data



commands = {
    "greeting": ["привет", "здравствуй", "здравствуйте", "хай"],
    "farewell": ["спасибо", "пока", "свидания", "прощай", "бай"] ,
    "grant": ["грант", "заявка", "заявку", "заявке", "заявки", "подать"],
    "project": ["создать", "проект", "проекта", "проекты", "проектов", "добавить"],
    "faq": ["проблема", "проблемы", "технические", "техническая", "вопрос", "вопросы", "вопросов", "вопросах"],
    "agreement": ["да", "ага", "конечно"],
    "disagreement": ["нет", "неа"],
    "help": ["помощь"]
}




if __name__ == "__main__":

    # инициализация инструментов распознавания и ввода речи
    recognizer = speech_recognition.Recognizer()
    microphone = speech_recognition.Microphone()

    # инициализация инструмента синтеза речи
    ttsEngine = pyttsx3.init()

    # настройка данных голосового помощника
    assistant = VoiceAssistant()
    assistant.name = "Alice"
    assistant.sex = "female"
    assistant.speech_language = "ru"

    # установка голоса по умолчанию



    setup_assistant_voice()
    play_voice_assistant_speech("Здравствуйте, чем я могу вам помочь?")
    while True:


        pointer = True #данная переменная предназначена для обозначения, нужно ли продолжать цикл для поддержания диалога с пользователем или нет
        # старт записи речи с последующим выводом распознанной речи
        # и удалением записанного в микрофон аудио
        voice_input = record_and_recognize_audio()
        os.remove("microphone-results.wav")
        print(voice_input)

        # отделение комманд от дополнительной информации (аргументов)
        voice_input = voice_input.split(" ")
        command = voice_input
        print(command)


        for key in commands.keys():
            for i in range(len(command)):
                if command[i] in commands[key]:

                    if key == "greeting":
                        play_voice_assistant_speech("Здравствуйте, могу ли я вам чем-то помочь?")
                        break

                    elif key == "farewell":
                        play_voice_assistant_speech("Если понадобится помощь, обращайтесь")
                        break

                    elif key == "grant":
                        play_voice_assistant_speech("Чтобы подать заявку на грант, необходимо зайти на вкладку Мои проекты и нажать кнопку подать заявку на грант. Для выполнения этого шага у вас должен быть зарегестрирован проект")
                        play_voice_assistant_speech("Если вам нужна помощь при заполнении заявки, скажите помощь")
                        break

                    elif key == "project":
                        play_voice_assistant_speech("Для того, чтобы добавить проект, перейдите на вкладку Мои проекты и нажмите по кнопке Добавить проект")
                        play_voice_assistant_speech("Если вам нужна помощь при регистрации проекта, скажите помощь")
                        break
                    
                    elif key == "help":
                        play_voice_assistant_speech("Перевожу вас на вкладку заполнения формы")

                    elif key == "faq":
                        play_voice_assistant_speech("Перевожу вас на вкладку часто задаваемых вопросов. Если вы не нашли ответ на свой вопрос, вы можете прислать нам на почту скриншот экрана где видна ошибка которую вы встречаете, не забудьте указать ID вашего аккаунта")
                        print("support@myrosmol.ru")
                        break

                        
                





