import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

const IntensityLineChart = ({ data }) => {
  return (
    <div className="bg-white rounded-lg shadow-sm p-6">
      <h2 className="text-xl font-semibold text-gray-900 mb-4">Monthly Emissions Trend</h2>
      <div className="h-64">
        <ResponsiveContainer width="100%" height="100%">
          <LineChart data={data}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="month" />
            <YAxis />
            <Tooltip />
            <Line 
              type="monotone" 
              dataKey="emissions" 
              stroke="#8884d8" 
              strokeWidth={2}
              name="Total Emissions"
            />
          </LineChart>
        </ResponsiveContainer>
      </div>
      {data && data.length > 0 && (
        <div className="mt-4 text-sm text-gray-600">
          <p>
            <span className="font-medium">Latest Month: </span>
            {data[data.length - 1]?.emissions.toFixed(0)} kgCO₂e
          </p>
        </div>
      )}
    </div>
  );
};

export default IntensityLineChart;