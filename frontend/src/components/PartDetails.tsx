import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { 
  Grid, 
  Card, 
  CardContent, 
  Typography,
  Box,
  Paper,
  Skeleton,
  Chip,
  Divider,
  useTheme,
  alpha,
  Tooltip
} from '@mui/material';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import { Build as BuildIcon, LocationOn as LocationIcon, AccessTime as TimeIcon, Scale as ScaleIcon, AttachMoney as MoneyIcon, Business as BusinessIcon } from '@mui/icons-material';
import { Part } from '../types';

const PartDetails: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();
  const [part, setPart] = useState<Part | null>(null);
  const [loading, setLoading] = useState(true);
  const theme = useTheme();

  useEffect(() => {
    const fetchPart = async () => {
      try {
        setLoading(true);
        const response = await fetch(`http://localhost:5001/api/parts/${id}`);
        const data = await response.json();
        setPart(data);
      } catch (error) {
        console.error('Error fetching part:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchPart();
  }, [id]);

  if (loading) {
    return (
      <Box>
        <Paper 
          elevation={0} 
          sx={{ 
            p: 3, 
            mb: 4, 
            borderRadius: 2,
            background: `linear-gradient(90deg, ${alpha(theme.palette.primary.main, 0.1)} 0%, ${alpha(theme.palette.background.paper, 0.05)} 100%)`,
            border: `1px solid ${alpha(theme.palette.divider, 0.1)}`
          }}
        >
          <Skeleton variant="text" width="40%" height={40} />
          <Skeleton variant="text" width="60%" />
        </Paper>
        <Grid container spacing={3}>
          <Grid item xs={12} md={6}>
            <Skeleton variant="rectangular" height={400} />
          </Grid>
          <Grid item xs={12} md={6}>
            <Skeleton variant="rectangular" height={400} />
          </Grid>
        </Grid>
      </Box>
    );
  }

  if (!part) {
    return (
      <Paper 
        elevation={0} 
        sx={{ 
          p: 4, 
          textAlign: 'center',
          borderRadius: 2,
          background: `linear-gradient(90deg, ${alpha(theme.palette.error.main, 0.1)} 0%, ${alpha(theme.palette.background.paper, 0.05)} 100%)`,
          border: `1px solid ${alpha(theme.palette.error.main, 0.2)}`
        }}
      >
        <Typography variant="h5" color="error" gutterBottom>
          Part Not Found
        </Typography>
        <Typography variant="body1" color="text.secondary">
          The requested part could not be found. Please try again or return to the product list.
        </Typography>
      </Paper>
    );
  }

  return (
    <Box>
      <Paper 
        elevation={0} 
        sx={{ 
          p: 3, 
          mb: 4, 
          borderRadius: 2,
          background: `linear-gradient(90deg, ${alpha(theme.palette.primary.main, 0.1)} 0%, ${alpha(theme.palette.background.paper, 0.05)} 100%)`,
          border: `1px solid ${alpha(theme.palette.divider, 0.1)}`
        }}
      >
        <Box sx={{ display: 'flex', alignItems: 'center', mb: 2 }}>
          <BuildIcon sx={{ mr: 2, color: 'primary.main' }} />
          <Typography variant="h5" component="h1" sx={{ fontWeight: 600 }}>
            {part.name}
          </Typography>
        </Box>
        <Box sx={{ display: 'flex', alignItems: 'center', mb: 2 }}>
          <Chip 
            label={part.sourceLocation.name} 
            size="small" 
            color="secondary" 
            variant="outlined"
            icon={<LocationIcon />}
          />
        </Box>
      </Paper>
      
      <Grid container spacing={3}>
        <Grid item xs={12} md={6}>
          <Paper 
            elevation={0} 
            sx={{ 
              p: 3, 
              mb: 3, 
              borderRadius: 2,
              background: theme.palette.background.paper,
              border: `1px solid ${alpha(theme.palette.divider, 0.1)}`
            }}
          >
            <Box sx={{ display: 'flex', alignItems: 'center', mb: 2 }}>
              <BusinessIcon sx={{ mr: 2, color: 'primary.main' }} />
              <Typography variant="h6" sx={{ fontWeight: 600 }}>
                Suppliers
              </Typography>
            </Box>
            <Divider sx={{ mb: 3 }} />
            <Grid container spacing={2}>
              {part.suppliers && part.suppliers.length > 0 ? (
                part.suppliers.map((supplier) => (
                  <Grid item xs={12} sm={6} key={supplier.id}>
                    <Tooltip 
                      title="Click to view supplier details and performance metrics"
                      arrow
                      placement="top"
                    >
                      <Card 
                        onClick={() => navigate(`/supplier/${supplier.id}`)}
                        sx={{ 
                          cursor: 'pointer',
                          transition: 'all 0.3s ease',
                          '&:hover': {
                            transform: 'translateY(-4px)',
                            boxShadow: `0 8px 16px ${alpha(theme.palette.common.black, 0.2)}`,
                            borderColor: theme.palette.primary.main
                          },
                          border: `1px solid ${alpha(theme.palette.divider, 0.1)}`,
                          borderRadius: 2
                        }}
                      >
                        <CardContent>
                          <Typography variant="subtitle1" sx={{ fontWeight: 600 }}>
                            {supplier.name}
                          </Typography>
                          <Box sx={{ display: 'flex', alignItems: 'center', mt: 1 }}>
                            <Chip 
                              label={supplier.location.name} 
                              size="small" 
                              color="secondary" 
                              variant="outlined"
                              icon={<LocationIcon />}
                            />
                          </Box>
                        </CardContent>
                      </Card>
                    </Tooltip>
                  </Grid>
                ))
              ) : (
                <Grid item xs={12}>
                  <Typography variant="body1" color="text.secondary" align="center">
                    No suppliers available for this part.
                  </Typography>
                </Grid>
              )}
            </Grid>
          </Paper>
        </Grid>

        <Grid item xs={12} md={6}>
          <Paper 
            elevation={0} 
            sx={{ 
              p: 3, 
              mb: 3, 
              borderRadius: 2,
              background: theme.palette.background.paper,
              border: `1px solid ${alpha(theme.palette.divider, 0.1)}`
            }}
          >
            <Box sx={{ display: 'flex', alignItems: 'center', mb: 2 }}>
              <LocationIcon sx={{ mr: 2, color: 'primary.main' }} />
              <Typography variant="h6" sx={{ fontWeight: 600 }}>
                Supplier Locations
              </Typography>
            </Box>
            <Divider sx={{ mb: 3 }} />
            <Box sx={{ height: 400, width: '100%', borderRadius: 2, overflow: 'hidden' }}>
              <MapContainer
                center={[20, 0]}
                zoom={2}
                style={{ height: '100%', width: '100%' }}
              >
                <TileLayer
                  url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                  attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                />
                
                {/* Source Location Marker */}
                <Marker
                  position={[part.sourceLocation.latitude, part.sourceLocation.longitude]}
                >
                  <Popup>
                    <Typography variant="subtitle2" sx={{ fontWeight: 600 }}>
                      Source Location
                    </Typography>
                    <Typography variant="body2">
                      {part.sourceLocation.name}
                    </Typography>
                  </Popup>
                </Marker>

                {/* Supplier Locations */}
                {part.suppliers && part.suppliers.map((supplier) => (
                  <Marker
                    key={supplier.id}
                    position={[supplier.location.latitude, supplier.location.longitude]}
                  >
                    <Popup>
                      <Typography variant="subtitle2" sx={{ fontWeight: 600 }}>
                        {supplier.name}
                      </Typography>
                      <Typography variant="body2">
                        {supplier.location.name}
                      </Typography>
                    </Popup>
                  </Marker>
                ))}
              </MapContainer>
            </Box>
          </Paper>
        </Grid>
      </Grid>
    </Box>
  );
};

export default PartDetails; 