import React from 'react';
import { Drawer, List, ListItemButton, ListItemText, Box } from '@mui/material';

const Sidebar = ({ onSelectGraph }: { onSelectGraph: (graphType: string) => void }) => {
  return (
    <Drawer
      sx={{
        width: 240,
        flexShrink: 0,
        '& .MuiDrawer-paper': {
          width: 240,
          boxSizing: 'border-box',
          paddingTop: '64px', // Padding to avoid top bar overlap
        },
      }}
      variant="permanent"
      anchor="left"
    >
      <List>
        <ListItemButton onClick={() => onSelectGraph('ActivityToRevenue')}>
          <ListItemText primary="Activity to Revenue" />
        </ListItemButton>
        <ListItemButton onClick={() => onSelectGraph('LocationToRevenue')}>
          <ListItemText primary="Location to Revenue" />
        </ListItemButton>
        <ListItemButton onClick={() => onSelectGraph('RevenueOverTime')}>
          <ListItemText primary="Revenue Over Time" />
        </ListItemButton>
        {/* Add more buttons as needed */}
      </List>
    </Drawer>
  );
};

export default Sidebar;
