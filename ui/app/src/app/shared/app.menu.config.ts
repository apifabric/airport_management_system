import { MenuRootItem } from 'ontimize-web-ngx';

import { AirplaneCardComponent } from './Airplane-card/Airplane-card.component';

import { AirportCardComponent } from './Airport-card/Airport-card.component';

import { FlightCardComponent } from './Flight-card/Flight-card.component';

import { PassengerCardComponent } from './Passenger-card/Passenger-card.component';


export const MENU_CONFIG: MenuRootItem[] = [
    { id: 'home', name: 'HOME', icon: 'home', route: '/main/home' },
    
    {
    id: 'data', name: ' data', icon: 'remove_red_eye', opened: true,
    items: [
    
        { id: 'Airplane', name: 'AIRPLANE', icon: 'view_list', route: '/main/Airplane' }
    
        ,{ id: 'Airport', name: 'AIRPORT', icon: 'view_list', route: '/main/Airport' }
    
        ,{ id: 'Flight', name: 'FLIGHT', icon: 'view_list', route: '/main/Flight' }
    
        ,{ id: 'Passenger', name: 'PASSENGER', icon: 'view_list', route: '/main/Passenger' }
    
    ] 
},
    
    { id: 'settings', name: 'Settings', icon: 'settings', route: '/main/settings'}
    ,{ id: 'about', name: 'About', icon: 'info', route: '/main/about'}
    ,{ id: 'logout', name: 'LOGOUT', route: '/login', icon: 'power_settings_new', confirm: 'yes' }
];

export const MENU_COMPONENTS = [

    AirplaneCardComponent

    ,AirportCardComponent

    ,FlightCardComponent

    ,PassengerCardComponent

];