import { useState } from '@lynx-js/react';

interface DropdownItemProps {
  label: string;
  isSelected: boolean;
  onSelect: () => void;
}

export function DropdownItem({ label, isSelected, onSelect }: DropdownItemProps) {
  const [isPressed, setIsPressed] = useState<boolean>(false);

  const itemStyle = {
    padding: '8px 12px',
    backgroundColor: isPressed ? '#e6f3ff' : (isSelected ? '#2C2F36' : '#1A1D23'),
    borderRadius: '8px',
    color: isSelected ? '#00D2FF' : '#F5F5F7',
    marginRight: '8px',
    cursor: 'pointer',
    fontSize: '14px',
  };

  return (
    <list-item
      item-key={`dropdown-item-${label}`}
      key={`dropdown-item-${label}`}
      bindtap={() => onSelect()}
      bindtouchstart={() => setIsPressed(true)}
      bindtouchend={() => setIsPressed(false)}
      bindtouchcancel={() => setIsPressed(false)}
    >
      <text style={itemStyle}>{label}</text>
    </list-item>
  );
}
