import { useState } from '@lynx-js/react'
import './Chatbot.css'
import Header from './Components/Header.tsx'
/// <reference types="@lynx-js/rspeedy/client" />

export default function Chatbot() {
  const [messages, setMessages] = useState([
    { sender: 'bot', text: 'Hello! How can I help you today?' },
  ])
  const [input, setInput] = useState('')

  const sendMessage = () => {
    if (!input.trim()) return

    // Add user message
    const newMessages = [...messages, { sender: 'user', text: input }]
    setMessages(newMessages)
    setInput('')

    // Simulate bot reply
    setTimeout(() => {
      setMessages(prev => [
        ...prev,
        { sender: 'bot', text: "I'm here to protect your privacy 🚀" },
      ])
    }, 800)
  }

  return (
    <view className="Background"> 
    <Header />
      <scroll-view scroll-y style="flex:1; height:100%;">
        <view className="Page"> 
          <view className="ChatContainer">
            <scroll-view className="ChatMessages" scroll-y>
              {messages.map((msg, index) => (
                <view
                  key={index}
                  className={msg.sender === 'user' ? 'UserBubble' : 'BotBubble'}
                >
                <text>{msg.text}</text>
                </view>
              ))}
            </scroll-view>

          <view className="ChatInputBar">
        
          <text className="SendButton" bindtap={sendMessage}>
          ➤
        </text>
      </view>
    </view>
    </view>
     </scroll-view>
    </view>
  )
}
