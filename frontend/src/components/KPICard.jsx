import React from 'react';
import { TrendingUp, Calendar, AlertCircle } from 'lucide-react';

const KPICard = ({ title, value, icon, color }) => {
  const getIcon = () => {
    switch (icon) {
      case 'TrendingUp':
        return <TrendingUp className="w-8 h-8" />;
      case 'Calendar':
        return <Calendar className="w-8 h-8" />;
      case 'AlertCircle':
        return <AlertCircle className="w-8 h-8" />;
      default:
        return <TrendingUp className="w-8 h-8" />;
    }
  };

  const getColorClasses = () => {
    switch (color) {
      case 'blue':
        return {
          text: 'text-blue-600',
          icon: 'text-blue-500'
        };
      case 'green':
        return {
          text: 'text-green-600',
          icon: 'text-green-500'
        };
      case 'red':
        return {
          text: 'text-red-600',
          icon: 'text-red-500'
        };
      default:
        return {
          text: 'text-blue-600',
          icon: 'text-blue-500'
        };
    }
  };

  const colorClasses = getColorClasses();

  return (
    <div className="bg-white rounded-lg shadow-sm p-6">
      <div className="flex items-center justify-between">
        <div>
          <p className="text-sm font-medium text-gray-600">{title}</p>
          <p className={`text-2xl font-bold ${colorClasses.text}`}>
            {value}
          </p>
        </div>
        <div className={colorClasses.icon}>
          {getIcon()}
        </div>
      </div>
    </div>
  );
};

export default KPICard;