import React, { useState, useEffect } from 'react';
import axios from 'axios'; // Import Axios
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, LineChart, Line, ResponsiveContainer, ComposedChart } from 'recharts';

const RevenueOverTimeGraph = () => {
  const [data, setData] = useState<{ quarter: string, revenue: number }[]>([]);
  const [loading, setLoading] = useState(true); // Handle loading state
  const [error, setError] = useState<string | null>(null); // Handle error state

  // Fetch data from the backend when the component mounts
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/data'); // Update your endpoint

        // Extract data from the 'performance' field
        const formattedData = Object.entries(response.data.companies[0].performance).map(([quarter, value]) => ({
          quarter,
          revenue: (value as { revenue: number }).revenue,
        }));

        setData(formattedData); // Set data from the API response
      } catch (err) {
        setError('Error fetching data'); // Handle error if the request fails
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

  return (
    <ResponsiveContainer width="100%" height={400}>
      <ComposedChart data={data}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="quarter" />
        <YAxis />
        <Tooltip />
        <Legend />
        {/* Bar for revenue */}
        <Bar dataKey="revenue" fill="#8884d8" />
        {/* Line for trend */}
        <Line type="monotone" dataKey="revenue" stroke="#ea76cb" strokeWidth={2} dot={true} />
      </ComposedChart>
    </ResponsiveContainer>
  );
};

export default RevenueOverTimeGraph;
