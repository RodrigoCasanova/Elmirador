import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';
import { FormsModule } from '@angular/forms'; // Para ngModel
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-gastos-comunes',
  imports: [CommonModule, FormsModule,  RouterModule],
  templateUrl: './gastos-comunes.component.html',
  styleUrls: ['./gastos-comunes.component.scss'],
})
export class GastosComunesComponent implements OnInit {
  gastosComunes: any[] = [];
  mes: number = 0; // Inicializamos mes y anio
  anio: number = 0;
  mostrarLista: boolean = false; // Controla la visibilidad de la lista

  constructor(private apiService: ApiService) {}

  ngOnInit(): void {
    this.obtenerGastosComunes();
  }

  crearGastosComunes(): void {
    const gasto = {
      mes: this.mes,
      anio: this.anio,
    };

    this.apiService.createGastosComunes(gasto).subscribe(
      (response) => {
        console.log('Gastos comunes creados con éxito:', response);
        alert(response.mensaje); // Mostramos mensaje de éxito
        this.obtenerGastosComunes(); // Actualizamos la lista después de crear
      },
      (error) => {
        console.error('Error al crear los gastos comunes:', error);
        alert('Error al crear los gastos comunes. ' + error.error.message);
      }
    );
  }

  obtenerGastosComunes(): void {
    this.apiService.getGastosComunes().subscribe((data) => {
      this.gastosComunes = data;
    });
  }

  toggleGastosComunes(): void {
    this.mostrarLista = !this.mostrarLista; // Alterna la visibilidad
    if (this.mostrarLista) {
      this.obtenerGastosComunes();
    }
  }
}
