export interface Product {
  id: number;
  name: string;
  description: string;
  parts: Part[];
  totalCost: number;
  deliveryTime: string;
  assemblyLocation: Location;
}

export interface Part {
  id: number;
  name: string;
  sourceLocation: Location;
  suppliers: Supplier[];
  deliveryTime: string;
  weight: number;
  price: number;
}

export interface Location {
  id: number;
  name: string;
  latitude: number;
  longitude: number;
}

export interface Supplier {
  id: number;
  name: string;
  location: Location;
} 