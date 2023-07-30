css = '''
<style>
.chat-box {
    max-height: 350px;
    overflow-y: auto;
    border: 2px solid #7A8089; /* A grayish border */
    border-radius: 5px; /* Rounded corners */
    box-shadow: 0px 0px 5px 0px #000000; /* Small black edges (shadow) */
    background-color: #F5F5F5; /* A grayish white background */
}
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

disclaimer_text = "The information provided by this chatbot may not be accurate, and users should verify critical details to ensure its reliability; the creators bear no liability for any consequences resulting from the use of this information."

box_template = '''
            <script>
            const chatBox = document.getElementById('chat-box');
            chatBox.scrollTop = chatBox.scrollHeight;
            </script>
        '''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://resources.mpi-inf.mpg.de/logo/logos/minerva.png">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://upload.wikimedia.org/wikipedia/commons/7/7c/Profile_avatar_placeholder_large.png">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''

user_img = "https://upload.wikimedia.org/wikipedia/commons/7/7c/Profile_avatar_placeholder_large.png"

bot_img = "https://resources.mpi-inf.mpg.de/logo/logos/minerva.png"