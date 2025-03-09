/// src/components/Mainpage.tsx
import React, { useState } from 'react';
import { Box, Container, Grid } from '@mui/material';
import TopBar from './Topbar';  
import ActivityToRevenueGraph from './Graphs/ActivityToRevenueGraph'; 
import LocationToRevenueGraph from './Graphs/LocationToRevenueGraph';
import Sidebar from './Sidebar';
import RevenueOverTimeGraph from './Graphs/RevenueOverTimeGraph';

const Mainpage = () => {

    const [selectedGraph, setSelectedGraph] = useState<string>('ActivityToRevenue'); // Default graph

    const handleSelectGraph = (graphType: string) => {
        setSelectedGraph(graphType); // Set the selected graph type
    };
    return (
        <Box sx={{ display: 'flex' }}>
        {/* Top Bar */}
        <TopBar /> 

        {/* Sidebar */}
        <Sidebar onSelectGraph={handleSelectGraph} /> {/* Passing the handler to Sidebar */}

        {/* Main Content */}
        <Box
            component="main"
            sx={{
            flexGrow: 1,
            bgcolor: 'background.default',
            marginLeft: '120px', // Sidebar width offset
            marginTop: '64px', // AppBar height offset
            }}
        >
            <Grid container spacing={2}>
            {/* Graph Section */}
            <Grid item xs={12}>
                <Container maxWidth="lg">
                {selectedGraph === 'LocationToRevenue' && <LocationToRevenueGraph></LocationToRevenueGraph>}
                {selectedGraph === 'ActivityToRevenue' && <ActivityToRevenueGraph></ActivityToRevenueGraph>}
                {selectedGraph === 'RevenueOverTime' && <RevenueOverTimeGraph></RevenueOverTimeGraph>}
                </Container>
            </Grid>
            </Grid>
        </Box>
        </Box>
    );
};

export default Mainpage;
