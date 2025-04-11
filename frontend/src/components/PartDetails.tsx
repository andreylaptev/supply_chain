import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { 
  Container, 
  Grid, 
  Card, 
  CardContent, 
  Typography,
  Box
} from '@mui/material';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import { Part } from '../types';

const PartDetails: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const [part, setPart] = useState<Part | null>(null);

  useEffect(() => {
    const fetchPart = async () => {
      try {
        const response = await fetch(`http://localhost:5001/api/parts/${id}`);
        const data = await response.json();
        setPart(data);
      } catch (error) {
        console.error('Error fetching part:', error);
      }
    };

    fetchPart();
  }, [id]);

  if (!part) {
    return <Typography>Loading...</Typography>;
  }

  return (
    <Container maxWidth="lg" sx={{ py: 4 }}>
      <Typography variant="h4" component="h1" gutterBottom sx={{ mb: 4 }}>
        {part.name}
      </Typography>
      
      <Grid container spacing={3}>
        <Grid item xs={12} md={6}>
          <Card sx={{ mb: 3 }}>
            <CardContent>
              <Typography variant="h6" gutterBottom>
                Part Details
              </Typography>
              <Typography variant="body1">
                Delivery Time: {part.deliveryTime}
              </Typography>
              <Typography variant="body1">
                Weight: {part.weight} kg
              </Typography>
              <Typography variant="body1">
                Price: ${part.price}
              </Typography>
            </CardContent>
          </Card>
        </Grid>

        <Grid item xs={12} md={6}>
          <Typography variant="h6" gutterBottom>
            Location Map
          </Typography>
          <Box sx={{ height: 400, width: '100%' }}>
            <MapContainer
              center={[part.sourceLocation.latitude, part.sourceLocation.longitude]}
              zoom={4}
              style={{ height: '100%', width: '100%' }}
            >
              <TileLayer
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
              />
              
              <Marker
                position={[part.sourceLocation.latitude, part.sourceLocation.longitude]}
              >
                <Popup>
                  Source Location: {part.sourceLocation.name}
                </Popup>
              </Marker>
            </MapContainer>
          </Box>
        </Grid>
      </Grid>
    </Container>
  );
};

export default PartDetails; 