import React from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import { 
  AppBar, 
  Toolbar, 
  Typography, 
  Button, 
  Box,
  IconButton,
  useTheme,
  alpha
} from '@mui/material';
import { 
  Home as HomeIcon,
  Inventory as InventoryIcon,
  Build as BuildIcon,
  ArrowBack as ArrowBackIcon
} from '@mui/icons-material';

const Navigation: React.FC = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const theme = useTheme();
  
  const getPageTitle = () => {
    if (location.pathname === '/') return 'Supply Chain Dashboard';
    if (location.pathname.startsWith('/product/')) return 'Product Details';
    if (location.pathname.startsWith('/part/')) return 'Part Details';
    return 'Supply Chain Dashboard';
  };

  const showBackButton = location.pathname !== '/';

  return (
    <AppBar 
      position="static" 
      elevation={0}
      sx={{ 
        background: `linear-gradient(90deg, ${theme.palette.background.paper} 0%, ${alpha(theme.palette.primary.main, 0.1)} 100%)`,
        borderBottom: `1px solid ${alpha(theme.palette.divider, 0.1)}`
      }}
    >
      <Toolbar>
        {showBackButton && (
          <IconButton 
            edge="start" 
            color="inherit" 
            onClick={() => navigate(-1)}
            sx={{ mr: 2 }}
          >
            <ArrowBackIcon />
          </IconButton>
        )}
        
        <Typography variant="h6" component="div" sx={{ flexGrow: 1, fontWeight: 500 }}>
          {getPageTitle()}
        </Typography>
        
        <Box sx={{ display: 'flex', alignItems: 'center' }}>
          <Button 
            color="inherit" 
            startIcon={<HomeIcon data-testid="HomeIcon" />}
            onClick={() => navigate('/')}
            sx={{ 
              mx: 1,
              borderRadius: '8px',
              '&:hover': {
                backgroundColor: alpha(theme.palette.common.white, 0.1)
              }
            }}
          >
            Dashboard
          </Button>
          <Button 
            color="inherit" 
            startIcon={<InventoryIcon data-testid="InventoryIcon" />}
            onClick={() => navigate('/')}
            sx={{ 
              mx: 1,
              borderRadius: '8px',
              '&:hover': {
                backgroundColor: alpha(theme.palette.common.white, 0.1)
              }
            }}
          >
            Products
          </Button>
          <Button 
            color="inherit" 
            startIcon={<BuildIcon data-testid="BuildIcon" />}
            onClick={() => navigate('/')}
            sx={{ 
              mx: 1,
              borderRadius: '8px',
              '&:hover': {
                backgroundColor: alpha(theme.palette.common.white, 0.1)
              }
            }}
          >
            Parts
          </Button>
        </Box>
      </Toolbar>
    </AppBar>
  );
};

export default Navigation; 