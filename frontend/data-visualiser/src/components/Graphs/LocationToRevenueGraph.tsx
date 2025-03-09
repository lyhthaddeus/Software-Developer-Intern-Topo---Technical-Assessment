import React, { useState, useEffect } from 'react';
import axios from 'axios'; 
import { Button } from '@mui/material';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, PieChart, Pie, Cell} from 'recharts';

const COLORS = ['#dc8a78', '#8839ef', '#179299', '#04a5e5'];

const LocationToRevenueGraph: React.FC = () => {
  const [data, setData] = useState<{ location: string, revenue: number }[]>([]);
  const [loading, setLoading] = useState(true); // Handle loading state
  const [error, setError] = useState<string | null>(null); // Handle error state
  const [chartType, setChartType] = useState<'bar' | 'pie'>('bar'); // Manage chart type state

  // Fetch data from the backend when the component mounts
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/utils/location_to_revenue');
        const formattedData = Object.entries(response.data.total_revenue_per_location).map(([location, revenue]) => ({
          location,
          revenue: parseFloat(Number(revenue).toFixed(2))
        }));
        setData(formattedData); 
      } catch (err) {
        setError('Error fetching data'); 
      } finally {
        setLoading(false); // Stop loading after request completes
      }
    };

    fetchData(); // Call the fetch function
  }, []);

  if (loading) {
    return <div>Loading...</div>; // Show loading text while fetching
  }

  if (error) {
    return <div>{error}</div>; // Show error if something went wrong
  }

  const toggleChartType = () => {
    setChartType((prevType) => (prevType === 'bar' ? 'pie' : 'bar'));
  };

  return (
    <div>
      <Button onClick={toggleChartType}>
        Toggle Chart Type
      </Button>
      <ResponsiveContainer width="100%" height={400}>
        {chartType === 'bar' ? (
          <BarChart data={data}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="location" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Bar dataKey="revenue" fill="#8884d8" />
          </BarChart>
        ) : (
          <PieChart>
            <Pie data={data} dataKey="revenue" nameKey="location" cx="50%" cy="50%" outerRadius={150} fill="#8884d8" label>
              {data.map((entry, index) => (
                <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
              ))}
            </Pie>
            <Tooltip />
            <Legend />
          </PieChart>
        )}
      </ResponsiveContainer>
    </div>
  );
};

export default LocationToRevenueGraph;
