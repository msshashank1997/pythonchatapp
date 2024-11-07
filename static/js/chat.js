const socket = io();

socket.on('message', function(data) {
    const messageElement = document.createElement("div");
    messageElement.classList.add("message");

    const messageContent = document.createElement("p");
    messageContent.innerHTML = `<strong>${data.user}</strong>: ${data.message} <span class="timestamp">${data.time}</span>`;

    messageElement.appendChild(messageContent);
    document.getElementById("messagesList").appendChild(messageElement);

    // Auto-scroll to the bottom of the chat
    document.getElementById("messagesList").scrollTop = document.getElementById("messagesList").scrollHeight;
});

function sendMessage() {
    const user = document.getElementById("userInput").value;
    const message = document.getElementById("messageInput").value;
    if (!user || !message) return; // Require both user and message

    socket.emit('message', {user: user, message: message});
    document.getElementById("messageInput").value = ''; // Clear message input
}