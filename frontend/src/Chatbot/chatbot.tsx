import { useState } from '@lynx-js/react'
import './Chatbot.css'
import Header from './Components/Header.tsx'
/// <reference types="@lynx-js/rspeedy/client" />

export default function Chatbot() {
  const [messages, setMessages] = useState([
    { sender: 'bot', text: 'Hello! How can I help you today?' },
  ])
  const [inputContent, setInputContent] = useState("")

  const sendMessage = () => {
  if (!inputContent.trim()) return

  const newMessages = [...messages, { sender: 'user', text: inputContent }]
  setMessages(newMessages)
  setInputContent('')

  const el = document.getElementById("chat-textarea") as HTMLTextAreaElement
  if (el) {
    el.value = ""  // clear 
    el.style.height = "auto"
  }

  setTimeout(() => {
    setMessages(prev => [...prev, { sender: 'bot', text: `You said: ${inputContent}` }])
  }, 600)
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
              <view style={{ flex: 1, padding: 8 }}>
                <textarea
                  className="ChatInput"
                  id="chat-textarea"
                  placeholder="Type a message..."
                  value={inputContent}
                  bindinput={(res: any) => {
                    const value = res.detail.value
                    setInputContent(value)

                    const el = document.getElementById("chat-textarea") as HTMLTextAreaElement
                    if (el) {
                      el.style.height = "auto"
                      el.style.height = Math.min(el.scrollHeight, 120) + "px"
                    }
                  }}
                  bindkeydown={(e: any) => {
                    if (e.key === "Enter" && !e.shiftKey) {
                      e.preventDefault?.() 
                      sendMessage()
                    }
                  }}
                  rows={1}
                  style="resize: none; overflow:hidden;"
                />
              </view>
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
