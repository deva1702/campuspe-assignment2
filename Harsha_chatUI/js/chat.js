
$(document).ready(function() {

    // DOM Elements

    const $messagesWrapper = $('#messagesWrapper');
    const $messagesContainer = $('#messagesContainer');
    const $messageInput = $('#messageInput');
    const $sendBtn = $('#sendBtn');
    const $welcomeScreen = $('#welcomeScreen');
    const $typingIndicator = $('#typingIndicator');
    const $sidebar = $('#sidebar');
    const $sidebarOverlay = $('#sidebarOverlay');
    const $menuToggle = $('#menuToggle');
    const $newChatBtn = $('#newChatBtn');
    const $themeToggle = $('#themeToggle');
    const $suggestionCards = $('.suggestion-card');

    // Chat Storage

    let chats = [];
    let currentChat = [];
    let chatCount = 1;
    let currentChatId = null;
    let isLoadingChat = false; // ⭐ NEW FIX

    // Mock AI Responses

    const aiResponses = [
        "That's a great question! Let me explain this in detail.",
        "I'd be happy to help with that!",
        "Excellent choice of topic!",
        "Thanks for asking!",
        "That's an interesting query!",
        "I appreciate your curiosity!",
        "Great question!",
        "I'm glad you asked about this!"
    ];

    const codeResponse = `Here's an example:

\`\`\`javascript
function greetUser(name) {
    return \`Hello, \${name}!\`;
}
\`\`\``;

    // Utility Functions

    function getCurrentTime() {
        const now = new Date();
        return now.toLocaleTimeString('en-US', {
            hour: 'numeric',
            minute: '2-digit',
            hour12: true
        });
    }

    function getRandomResponse() {
        return aiResponses[Math.floor(Math.random() * aiResponses.length)];
    }

    function formatMessage(text) {
        text = text.replace(/```(\w+)?\n([\s\S]*?)```/g, '<pre><code>$2</code></pre>');
        text = text.replace(/`([^`]+)`/g, '<code>$1</code>');
        text = text.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
        text = text.replace(/\*([^*]+)\*/g, '<em>$1</em>');
        text = text.replace(/\n/g, '<br>');
        return text;
    }

    function scrollToBottom() {
        $messagesContainer.animate({
            scrollTop: $messagesContainer[0].scrollHeight
        }, 300);
    }

    // Message Display

    function addMessage(text, sender) {
        const time = getCurrentTime();
        const name = sender === 'user' ? 'You' : 'ChatAI';
        const icon = sender === 'user' ? 'fa-user' : 'fa-robot';
        const formattedText = formatMessage(text);

        const messageHTML = `
            <div class="message ${sender}">
                <div class="message-avatar">
                    <i class="fas ${icon}"></i>
                </div>
                <div class="message-content">
                    <div class="message-header">
                        <span class="message-name">${name}</span>
                        <span class="message-time">${time}</span>
                    </div>
                    <div class="message-bubble">
                        ${formattedText}
                    </div>
                </div>
            </div>
        `;

        $messagesWrapper.append(messageHTML);
        scrollToBottom();

        currentChat.push({ text, sender });

        // ⭐ Prevent overwrite during loading
        if (!isLoadingChat && currentChatId !== null) {
            const chat = chats.find(c => c.id === currentChatId);
            if (chat) {
                chat.messages = [...currentChat];
            }
        }
    }

    // Typing Indicator

    function showTypingIndicator() {
        $typingIndicator.addClass('active');
    }

    function hideTypingIndicator() {
        $typingIndicator.removeClass('active');
    }

    // Send Message

    function sendMessage() {
        const text = $messageInput.val().trim();
        if (!text) return;

        if ($welcomeScreen.is(':visible')) {
            $welcomeScreen.addClass('hidden');
        }

        addMessage(text, 'user');

        $messageInput.val('').css('height', 'auto');
        $sendBtn.prop('disabled', true);

        showTypingIndicator();

        setTimeout(function() {
            hideTypingIndicator();

            const isCode = /code|javascript|html|css/i.test(text);
            const response = isCode ? codeResponse : getRandomResponse();

            addMessage(response, 'assistant');
        }, 1200);
    }

    // Input Handling
    $messageInput.on('input', function() {
        const hasText = $(this).val().trim().length > 0;
        $sendBtn.prop('disabled', !hasText);

        this.style.height = 'auto';
        this.style.height = Math.min(this.scrollHeight, 200) + 'px';
    });

    $messageInput.on('keydown', function(e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });

    $sendBtn.on('click', sendMessage);

    // Suggestion Cards

    $suggestionCards.on('click', function() {
        const suggestion = $(this).data('suggestion');

        $newChatBtn.click();
        $messageInput.val(suggestion).trigger('input');
        sendMessage();
    });

    // New Chat

    $newChatBtn.on('click', function() {

        if (currentChat.length > 0 && currentChatId === null) {
            chats.push({
                id: chatCount,
                messages: [...currentChat]
            });

            $('#chatHistory').prepend(`
                <div class="history-item" data-id="${chatCount}">
                    <i class="fas fa-message"></i>
                    <span>${currentChat[0].text.substring(0, 20)}...</span>
                </div>
            `);

            chatCount++;
        }

        currentChat = [];
        currentChatId = null;

        $messagesWrapper.find('.message').remove();
        $welcomeScreen.removeClass('hidden');
    });

    // Load Chat
    $(document).on('click', '.history-item', function() {
        const id = $(this).data('id');

        if (currentChat.length > 0 && currentChatId === null) {
            chats.push({
                id: chatCount,
                messages: [...currentChat]
            });

            $('#chatHistory').prepend(`
                <div class="history-item" data-id="${chatCount}">
                    <i class="fas fa-message"></i>
                    <span>${currentChat[0].text.substring(0, 20)}...</span>
                </div>
            `);

            chatCount++;
        }

        const selectedChat = chats.find(chat => chat.id == id);
        if (!selectedChat) return;

        $messagesWrapper.find('.message').remove();
        $welcomeScreen.addClass('hidden');

        // ⭐ FIX START
        isLoadingChat = true;

        selectedChat.messages.forEach(msg => {
            addMessage(msg.text, msg.sender);
        });

        isLoadingChat = false;


        currentChat = [...selectedChat.messages];
        currentChatId = id;
    });

    // Sidebar Toggle
    $menuToggle.on('click', function() {
        $sidebar.addClass('active');
        $sidebarOverlay.addClass('active');
    });

    $sidebarOverlay.on('click', function() {
        $sidebar.removeClass('active');
        $sidebarOverlay.removeClass('active');
    });

    // Dark Mode
    const savedTheme = localStorage.getItem('theme');

    if (savedTheme === 'dark') {
        $('body').attr('data-theme', 'dark');
    }

    $themeToggle.on('click', function() {
        const isDark = $('body').attr('data-theme') === 'dark';

        if (isDark) {
            $('body').removeAttr('data-theme');
            localStorage.setItem('theme', 'light');
        } else {
            $('body').attr('data-theme', 'dark');
            localStorage.setItem('theme', 'dark');
        }
    });

    // Profile Menu
    $('#profileMenuBtn').on('click', function(e) {
        e.stopPropagation();
        $('#profileMenu').toggleClass('hidden');
    });

    $(document).on('click', function() {
        $('#profileMenu').addClass('hidden');
    });

});