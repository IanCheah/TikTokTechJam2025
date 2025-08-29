import { useState } from '@lynx-js/react'
import * as React from 'react'

function ChatPage() {
  const [messages, setMessages] = useState([
    { sender: "bot", text: "Hello! How can I help you today?" }
  ]);
  const [input, setInput] = useState("");
  const [search, setSearch] = useState("");

  const handleInput = (event: any) => {
    setSearch(event.detail.value);
  };

  const handleSend = () => {
    if (!input.trim()) return;

    // Add user message
    const newMessages = [...messages, { sender: "user", text: input }];
    setMessages(newMessages);

    // Reset input
    setInput("");

    // Mock bot reply (replace with backend call later)
    setTimeout(() => {
      setMessages(prev => [...prev, { sender: "bot", text: "Got it! 👍" }]);
    }, 500);
  };

  return (
    <view className="ChatPage" style={{ flex: 1, padding: 16, backgroundColor: "#f9f9f9" }}>
      
      {/* Scrollable chat area */}
      <scroll-view style={{ flex: 1, marginBottom: 12 }}>
        {messages.map((msg, index) => (
          <view 
            key={index} 
            style={{ 
              alignItems: msg.sender === "user" ? "flex-end" : "flex-start",
            }}
          >
            <view 
              style={{ 
                backgroundColor: msg.sender === "user" ? "#4f46e5" : "#e5e7eb",
                padding: 10,
                borderRadius: 12,
                maxWidth: "70%"
              }}
            >
              <text style={{ color: msg.sender === "user" ? "white" : "black" }}>
                {msg.text}
              </text>
            </view>
          </view>
        ))}
      </scroll-view>

      {/* Input row */}
       <view className="inputView">
        <input
          // @ts-ignore
          bindinput={handleInput}
          className="inputBox"
          placeholder="Search products here..."
          value={search}
        />
        {search && (
          <image
            bindtap={() => setSearch("")}
            src={close}
            className="closeIcon"
          />
        )}
      </view>
    </view>
  );
}

export default ChatPage;
