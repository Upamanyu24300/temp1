import React from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

const YoYBarChart = ({ data }) => {
  // Prepare YoY chart data
  const yoyChartData = data ? [
    {
      year: 'Previous Year',
      scope1: data.previous_year?.scope1 || 0,
      scope2: data.previous_year?.scope2 || 0
    },
    {
      year: 'Current Year',
      scope1: data.current_year?.scope1 || 0,
      scope2: data.current_year?.scope2 || 0
    }
  ] : [];

  return (
    <div className="bg-white rounded-lg shadow-sm p-6">
      <h2 className="text-xl font-semibold text-gray-900 mb-4">Year-over-Year Emissions</h2>
      <div className="h-64">
        <ResponsiveContainer width="100%" height="100%">
          <BarChart data={yoyChartData}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="year" />
            <YAxis />
            <Tooltip />
            <Bar dataKey="scope1" stackId="a" fill="#8884d8" name="Scope 1" />
            <Bar dataKey="scope2" stackId="a" fill="#82ca9d" name="Scope 2" />
          </BarChart>
        </ResponsiveContainer>
      </div>
      {data && (
        <div className="mt-4 text-sm text-gray-600">
          <p>
            <span className="font-medium">Change: </span>
            <span className={`${data.change_percentage >= 0 ? 'text-red-600' : 'text-green-600'}`}>
              {data.change_percentage?.toFixed(1)}%
            </span>
          </p>
        </div>
      )}
    </div>
  );
};

export default YoYBarChart;