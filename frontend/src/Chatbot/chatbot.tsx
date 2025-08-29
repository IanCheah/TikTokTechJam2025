import { useState } from '@lynx-js/react'
import './Chatbot.css'

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
    <view className="ChatContainer">
      <text> "hello"</text>
    </view>
  )
}
