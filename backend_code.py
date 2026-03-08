from google import genai
import scratchattach as sa

cloud = sa.get_tw_cloud("1288061323")
client = cloud.requests()

def run():
    client.start(thread=True)

def ai_response(user_chat):
    client = genai.Client(api_key="AIzaSyCBegCW4r25Aem-ZiN_slL34H0EUUX_UDA")
    response = client.models.generate_content(
        model="gemini-3-flash-preview", contents=str(user_chat)
    )
    return response.text

@client.request
def get_resp(inp): #called when client receives request
    print("Ping request received")
    return ai_response(str(inp)) #sends back 'pong' to the Scratch project

@client.event
def on_ready():
    print("Request handler is running")
