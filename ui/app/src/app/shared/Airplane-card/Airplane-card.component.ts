import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Airplane-card.component.html',
  styleUrls: ['./Airplane-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Airplane-card]': 'true'
  }
})

export class AirplaneCardComponent {


}