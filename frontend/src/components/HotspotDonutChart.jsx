import React from 'react';
import { PieChart, Pie, Cell, ResponsiveContainer, Tooltip } from 'recharts';

const COLORS = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042', '#8884D8'];

const HotspotDonutChart = ({ data }) => {
  // Prepare hotspot pie chart data - filter out zero values
  const hotspotChartData = data ? Object.entries(data)
    .filter(([key, value]) => value > 0) // Only include entries with value > 0
    .map(([key, value]) => ({
      name: key,
      value: value
    })) : [];

  return (
    <div className="bg-white rounded-lg shadow-sm p-6">
      <h2 className="text-xl font-semibold text-gray-900 mb-4">Emission Sources Breakdown</h2>
      <div className="h-64">
        <ResponsiveContainer width="100%" height="100%">
          <PieChart>
            <Pie
              data={hotspotChartData}
              cx="50%"
              cy="50%"
              innerRadius={60}
              outerRadius={80}
              paddingAngle={5}
              dataKey="value"
            >
              {hotspotChartData.map((entry, index) => (
                <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
              ))}
            </Pie>
            <Tooltip />
          </PieChart>
        </ResponsiveContainer>
      </div>
      {hotspotChartData.length > 0 && (
        <div className="mt-4">
          {hotspotChartData.map((entry, index) => (
            <div key={entry.name} className="flex items-center justify-between py-1">
              <div className="flex items-center">
                <div 
                  className="w-3 h-3 rounded-full mr-2"
                  style={{ backgroundColor: COLORS[index % COLORS.length] }}
                ></div>
                <span className="text-sm text-gray-600">{entry.name}</span>
              </div>
              <span className="text-sm font-medium">{entry.value.toFixed(1)} kgCO₂e</span>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default HotspotDonutChart;