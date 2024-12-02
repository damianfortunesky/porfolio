interface FormLabelProps {
    htmlFor: string;
    label: string;

}

const FormLabel: React.FC<FormLabelProps> = ({
    htmlFor,
    label,
}) => {
  return (
    <label className="block text-sm font-medium text-gray-700" htmlFor={htmlFor}>
    {label}
  </label>
  );
};

export default FormLabel;