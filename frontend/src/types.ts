export interface Product {
  id: string;
  name: string;
  parts: Part[];
  assemblyLocation: Location;
}

export interface Part {
  id: string;
  name: string;
  deliveryTime: string;
  weight: number;
  price: number;
  sourceLocation: Location;
}

export interface Location {
  id: string;
  name: string;
  latitude: number;
  longitude: number;
} 