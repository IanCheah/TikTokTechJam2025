import { useState } from '@lynx-js/react'
import './Chatbot.css'
import Header from './Components/Header.tsx'
import { DropdownItem } from '../Dropdown/dropdown.tsx'
/// <reference types="@lynx-js/rspeedy/client" />

interface PrivacyIssue {
  id: number;
  issue: string;
  location: string;
  severity: string;
  suggestion: string;
  implications: string;
}

interface LLMResponse {
  issues: PrivacyIssue[];
  raw_text: string;
  fixed_code?: string;
}

interface ChatRequest {
  type: string;
  request: string;
}


export default function Chatbot() {
    const [messages, setMessages] = useState([
        { sender: 'bot', text: 'Hello! How can I help you today?' },
    ])
    const [inputContent, setInputContent] = useState("")
    const [dropdownValue, setDropdownValue] = useState("suggestions")

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
        }, 0)
    }

    const sendToBackend = async (message: string, dropdownSelection: string) => {
        const chatRequest: ChatRequest = {
            type: dropdownSelection,
            request: message,
        }

        try {
            const response = await fetch('https://your-fastapi-endpoint-url.com/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(chatRequest)
            })

            if (!response.ok) {
                throw new Error('Failed to send data to backend')
            }

            const data: LLMResponse = await response.json()
            handleLLMResponse(data)

        } catch (error) {
            console.error('Error sending message:', error)
        }
    }

    const handleLLMResponse = (data: LLMResponse) => {
        console.log('Received LLM Response:', data)
        setMessages(prev => [
            ...prev,
            { sender: 'bot', text: data.raw_text },
            ...data.issues.map(issue => ({
                sender: 'bot',
                text: `Issue: ${issue.issue} (Severity: ${issue.severity})`,
            })),
        ])

        if (data.fixed_code) {
            setMessages(prev => [
                ...prev,
                { sender: 'bot', text: `Fixed Code: ${data.fixed_code}` }
            ])
        }
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

                        {/* Dropdown above textarea */}
                        <view className="DropdownContainer" style={{ padding: '8px' }}>
                            <DropdownItem 
                                label="Fixing"
                                isSelected={dropdownValue === 'fixing'}
                                onSelect={() => setDropdownValue('fixing')}
                            />
                            <DropdownItem 
                                label="Suggestion"
                                isSelected={dropdownValue === 'suggestions'}
                                onSelect={() => setDropdownValue('suggestion')}
                            />
                        </view>

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
