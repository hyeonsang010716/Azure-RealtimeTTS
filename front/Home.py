import streamlit as st

def main():
    st.title("Text-to-Speech Demo")

    # 예시 HTML/JS 코드
    # (아래 엔드포인트: http://127.0.0.1:8000 은 FastAPI 서버가 동작 중이라고 가정)
    html_code = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Text-To-Speech</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
                margin: 0;
                padding: 0;
            }
            h2 {
                color: #333;
                text-align: center;
            }
            #container {
                width: 80%;
                margin: 50px auto;
                background-color: #fff;
                border-radius: 10px;
                padding: 20px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            label {
                font-weight: bold;
            }
            select, textarea {
                width: 100%;
                padding: 10px;
                margin: 10px 0;
                border: 1px solid #ccc;
                border-radius: 5px;
                box-sizing: border-box;
                font-size: 16px;
            }
            button {
                display: block;
                width: 100%;
                padding: 15px;
                background-color: #007bff;
                border: none;
                border-radius: 5px;
                color: #fff;
                font-size: 16px;
                cursor: pointer;
                transition: background-color 0.3s;
            }
            button:hover {
                background-color: #0056b3;
            }
            audio {
                width: 80%;
                margin: 10px auto;
                display: block;
            }
        </style>
    </head>
    <body>
        <div id="container">
            <h2>Text to Speech</h2>
            <label for="engine">Select Engine:</label>
            <select id="engine">
                <option value="azure">azure</option>
            </select>
            <label for="voice">Select Voice:</label>
            <select id="voice">
                <option value="ko-KR-InJoonNeural">ko-KR-InJoonNeural</option>
                <option value="ko-KR-SunHiNeural">ko-KR-SunHiNeural</option>
            </select>
            <textarea id="text" rows="4" cols="50" placeholder="Enter text here..."></textarea>
            <button id="speakButton">Speak</button>
            <audio id="audio" controls></audio>
        </div>

        <script>
        async function setEngine() {
            var engine = document.getElementById("engine").value;
            await fetch('http://127.0.0.1:8000/set_engine?engine_name=' + engine);
        }

        async function speak() {
            var text = document.getElementById("text").value;
            try {
                var url = 'http://127.0.0.1:8000/tts?text=' + encodeURIComponent(text);
                var audio = document.getElementById("audio");
                audio.src = url;
                audio.play();
            } catch (error) {
                console.error('Error during fetch or audio playback:', error);
            }
        }

        async function fetchVoices() {
            try {
                var response = await fetch('http://127.0.0.1:8000/voices');
                if (!response.ok) {
                    throw new Error('Network response was not ok: ' + response.statusText);
                }
                var data = await response.json();
                var voicesDropdown = document.getElementById("voice");
                voicesDropdown.innerHTML = ''; // Clear previous options
                data.forEach(function(voice) {
                    var option = document.createElement("option");
                    option.text = voice;
                    option.value = voice;
                    voicesDropdown.add(option);
                });
            } catch (error) {
                console.error('Error fetching voices:', error);
            }
        }

        async function setVoice() {
            var voice = document.getElementById("voice").value;
            try {
                var response = await fetch('http://127.0.0.1:8000/setvoice?voice_name=' + encodeURIComponent(voice));
                if (!response.ok) {
                    throw new Error('Network response was not ok: ' + response.statusText);
                }
                console.log('Voice set successfully:', voice);
            } catch (error) {
                console.error('Error setting voice:', error);
            }
        }

        document.addEventListener('DOMContentLoaded', (event) => {
            document.getElementById("text").value = "This is a text to speech demo text";
            document.getElementById("speakButton").addEventListener("click", speak);
            document.getElementById("engine").addEventListener("change", async function() {
                await setEngine();
                await fetchVoices();
            });
            document.getElementById("voice").addEventListener("change", setVoice);

            // 초기 로드 시 목소리 목록 가져오기
            fetchVoices();
        });
        </script>
    </body>
    </html>
    """

    st.subheader("1) HTML 인터페이스 미리보기")
    st.components.v1.html(html_code, height=700, scrolling=True)

    st.subheader("2) HTML 파일 다운로드")
    st.download_button(
        label="Download HTML",
        data=html_code,
        file_name="tts_interface.html",
        mime="text/html"
    )

if __name__ == "__main__":
    main()
