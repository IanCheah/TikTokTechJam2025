// Header.tsx
import { useNavigate } from 'react-router'
import './Header.css'

export default function Header() {
  const navigate = useNavigate()

  const goBack = () => {
    navigate(-1) // go back to previous page
  }

  return (
    <view className="HeaderContainer">
      <text className="BackButton" bindtap={goBack}>
        ←
      </text>
      <text className="HeaderTitle">CapΔ</text>
      <view style="width:40px;" /> 
    </view>
  )
}
