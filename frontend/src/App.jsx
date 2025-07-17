import React, { useState, useEffect } from 'react';
import { Zap } from 'lucide-react';
import EmissionForm from './components/EmissionForm';
import YoYBarChart from './components/YoYBarChart';
import HotspotDonutChart from './components/HotspotDonutChart';
import IntensityLineChart from './components/IntensityLineChart';
import KPICard from './components/KPICard';

const API_BASE_URL = 'http://localhost:8000';

const App = () => {
  const [yoyData, setYoyData] = useState(null);
  const [intensityData, setIntensityData] = useState(null);
  const [hotspotData, setHotspotData] = useState(null);
  const [monthlyData, setMonthlyData] = useState([]);
  const [loading, setLoading] = useState(false);
  const [notification, setNotification] = useState('');

  // Fetch analytics data
  const fetchAnalytics = async () => {
    setLoading(true);
    try {
      const [yoyRes, intensityRes, hotspotRes] = await Promise.all([
        fetch(`${API_BASE_URL}/analytics/yoy`),
        fetch(`${API_BASE_URL}/analytics/intensity`),
        fetch(`${API_BASE_URL}/analytics/hotspot`)
      ]);

      if (yoyRes.ok) {
        const yoyResult = await yoyRes.json();
        setYoyData(yoyResult);
      }
      if (intensityRes.ok) {
        const intensityResult = await intensityRes.json();
        setIntensityData(intensityResult);
      }
      if (hotspotRes.ok) {
        const hotspotResult = await hotspotRes.json();
        setHotspotData(hotspotResult);
      }
    } catch (error) {
      console.error('Error fetching analytics:', error);
    } finally {
      setLoading(false);
    }
  };

  // Generate sample monthly data for demonstration
  const generateMonthlyData = () => {
    const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    const data = months.map(month => ({
      month,
      emissions: Math.floor(Math.random() * 1000) + 500,
      scope1: Math.floor(Math.random() * 400) + 200,
      scope2: Math.floor(Math.random() * 600) + 300
    }));
    setMonthlyData(data);
  };

  useEffect(() => {
    fetchAnalytics();
    generateMonthlyData();
  }, []);

  const handleFormSubmit = (message) => {
    setNotification(message);
    fetchAnalytics(); // Refresh analytics after submission
    setTimeout(() => setNotification(''), 3000);
  };

  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div className="bg-white rounded-lg shadow-sm p-6 mb-6">
          <div className="flex items-center justify-between">
            <div>
              <h1 className="text-3xl font-bold text-gray-900">Carbon Emissions Dashboard</h1>
              <p className="text-gray-600 mt-1">Track and analyze your organization's carbon footprint</p>
            </div>
            <div className="flex items-center space-x-2 text-green-600">
              <Zap className="w-6 h-6" />
              <span className="text-sm font-medium">ESG Reporting Platform</span>
            </div>
          </div>
        </div>

        {/* Notification */}
        {notification && (
          <div className="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded mb-6">
            {notification}
          </div>
        )}

        {/* KPI Cards */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
          <KPICard
            title="Emission Intensity"
            value={
                    intensityData && Object.keys(intensityData).length > 0
                      ? `${intensityData[Object.keys(intensityData).at(-1)].toFixed(2)} kgCO₂e/unit`
                      : 'Loading...'
                  }
            icon="TrendingUp"
            color="blue"
          />
          <KPICard
            title="Current Year Total"
            value={yoyData ? `${((yoyData.current_year?.scope1 || 0) + (yoyData.current_year?.scope2 || 0)).toFixed(0)} kgCO₂e` : 'Loading...'}
            icon="Calendar"
            color="green"
          />
          <KPICard
            title="YoY Change"
            value={yoyData ? `${yoyData.change_percentage?.toFixed(1) || 0}%` : 'Loading...'}
            icon="AlertCircle"
            color="red"
          />
        </div>

        {/* Main Content Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          {/* Data Input Form */}
          <EmissionForm onSubmit={handleFormSubmit} />

          {/* YoY Emissions Comparison */}
          <YoYBarChart data={yoyData} />

          {/* Emission Hotspot */}
          <HotspotDonutChart data={hotspotData} />

          {/* Monthly Emissions Trend */}
          <IntensityLineChart data={monthlyData} />
        </div>
      </div>
    </div>
  );
};

export default App;