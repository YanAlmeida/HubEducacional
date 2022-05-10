import React from 'react'
import ReactDOM from 'react-dom/client'
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import Home from './pages/Home'
import Register from './pages/Register'
import Login from './pages/Login'
import Documentos from './pages/Documentos/Documentos'
import DocumentosPost from './pages/Documentos/DocumentosPost'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home/>}/>
        <Route path="register" element={<Register/>}/>
        <Route path="login" element={<Login/>}/>
        <Route path="documentos" element={<Documentos/>}/>
        <Route path="documentos/post" element={<DocumentosPost/>}/>
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
)
