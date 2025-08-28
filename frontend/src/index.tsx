import '@lynx-js/preact-devtools'
import '@lynx-js/react/debug'
import { root } from '@lynx-js/react'
import {MemoryRouter, Routes, Route} from 'react-router'
import ChatPage from './pages/chatbot.js'
import { App } from './App.jsx'

root.render(
  <MemoryRouter>
    <Routes>
      <Route path = "/" element={<App />}/>
      <Route path = "/chatbot" element={<ChatPage />}/>
    </Routes>
  </MemoryRouter>

);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept()
}
