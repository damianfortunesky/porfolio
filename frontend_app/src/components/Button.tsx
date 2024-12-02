
interface ButtonProps {
  type?: 'button' | 'submit' | 'reset';
  onClick?: () => void;
  label: string;
  className?: string;
}

const defaultClassName = 'w-full px-3 py-2 bg-pink-500 text-white rounded-md';

const Button: React.FC<ButtonProps> = ({
  type = 'button', 
  onClick,
  label,
  className = '',
}) => {
  return (
    <button
      type={type}
      onClick={onClick}
      className={`${defaultClassName} ${className}`.trim()} // Combina estilos por defecto y opcionales
    >
      {label}
    </button>
  );
};

export default Button;