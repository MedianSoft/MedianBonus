interface StatsCardProps {
  title: string;
  value: string | number;
  color?: 'orange' | 'green' | 'default';
}

export const StatsCard = ({ title, value, color = 'default' }: StatsCardProps) => {
  const colorClasses = {
    orange: 'text-orange-500',
    green: 'text-green-500',
    default: 'text-black'
  };

  return (
    <div className="bg-app-surface p-6 rounded-2xl border border-gray-800 shadow-sm">
      <p className="text-sm mb-1">{title}</p>
      <p className={`text-3xl font-bold ${colorClasses[color]}`}>
        {value}
      </p>
    </div>
  );
};
