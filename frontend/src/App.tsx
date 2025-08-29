import { useCallback, useEffect, useState } from '@lynx-js/react'
import { useRef } from '@lynx-js/react'
import './App.css'
import arrow from './assets/arrow.png'
import ChatPage from './pages/chatbot.js'
import { useNavigate } from 'react-router'
import '@lynx-js/web-elements/all';
import '@lynx-js/web-elements/index.css';

export function App(props: {
  onRender?: () => void
}) {

  useEffect(() => {
    console.info('Hello, ReactLynx')
  }, [])
  props.onRender?.()

  const [scrollTarget, setScrollTarget] = useState('')

  const nav = useNavigate();

  return (
    <view className="Background">
      <scroll-view scroll-y style="flex:1; height:100%;" scroll-into-view={scrollTarget}>
        <view className="Page">

          {/* Navigation Bar */}
          <view className="Nav">
            <text className="TeamName">CapΔ</text>
            <view className="NavLinks">
              <text className="NavLink" bindtap={() => setScrollTarget('homeSection')}>Home</text>
              <text className="NavLink" bindtap={() => setScrollTarget('aboutSection')}>About</text>
              <text className="NavLink" bindtap={() => setScrollTarget('featuresSection')}>Features</text>
              <text className="CTA" bindtap={() => nav("/chatbot")}>Get Started</text>
            </view>
          </view>

          {/* Hero Section */}
          <view className='body'>
            <view id="homeSection"> 
              <view className="Hero">
                <view className="HeroText">
                  <text className="HeroTitle">Chat Freely.{"\n"}Stay Private.</text>
                  <text className="HeroSubtitle">Your AI chatbot that puts your data first.</text>
                  <text 
                    className="CTA" style="margin-top: 10px" bindtap={() => nav("/chatbot")}>Start Chatting</text>
                </view>
                <image src={arrow} className="HeroImage" />
              </view>
            </view>

            {/* About Section */}
            <view id="aboutSection">
              <text className="Subtitle">About</text>
              <text className="Description">CapΔ automatically detects and removes sensitive data from your images and code before you share them with LLMs like ChatGPT, ensuring your personal and proprietary information stays secure.</text>
            </view>
            
            {/* Features Section */}
            <view id="featuresSection"> 
              <text className="Subtitle">Features</text>
              <view className="Features"> 
                <view className="FeatureCard">
                  <text className="FeatureTitle">🔒 Privacy by Design</text>
                  <text className="FeatureText">End-to-end encryption</text>
                </view>
                <view className="FeatureCard">
                  <text className="FeatureTitle">🗑️ No Data Stored</text>
                  <text className="FeatureText">Conversations vanish when you close</text>
                </view>
                <view className="FeatureCard">
                  <text className="FeatureTitle">🤖 AI Powered</text>
                  <text className="FeatureText">Smart but safe</text>
                </view>
              </view>
            </view>

            {/* Chatbot Example */}
            <view className="Chatbox">
              <view className="BotBubble">
                <text>Hello! How can I help you today?</text>
              </view>
              <view className="UserBubble">
                <text>I want to remove sensitive information from my code</text>
              </view>
              <view className="ChatInput">
                <text className="InputPlaceholder">Type a message...</text>
                <text className="SendButton">➤</text>
              </view>
            </view>
          

            {/* Footer */}
            <view className="Footer">
              <text>Privacy Policy | Contact | TikTok Hackathon</text>
            </view>
          </view>
        </view>
      </scroll-view>
    </view>
  )
}