type InputFieldProps = {
    id: string;
    name: string;
    type: string;
    value: string;
    onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
    placeholder?: string;
  };
  
const InputField: React.FC<InputFieldProps> = ({
    id,
    name,
    type,
    value,
    onChange,
    placeholder,
  }) => (
    <input
      id={id}
      name={name}
      type={type}
      value={value}
      onChange={onChange}
      placeholder={placeholder}
      className="border rounded p-2 w-full"
    />
  );
  
export default InputField;
