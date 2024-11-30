  // listar-gastos-pendientes.component.ts
  import { Component, OnInit } from '@angular/core';
  import { ApiService } from '../api.service';
  import { FormsModule } from '@angular/forms'; // Para ngModel
  import { CommonModule } from '@angular/common';
  import { RouterModule } from '@angular/router';

  @Component({
    selector: 'app-listar-gastos-pendientes',
    imports: [CommonModule, FormsModule,  RouterModule],
    templateUrl: './listar-gastos-pendientes.component.html',
    styleUrls: ['./listar-gastos-pendientes.component.scss']
  })
  export class ListarGastosPendientesComponent {
    mes: number = 1;  // Valor por defecto
    anio: number = new Date().getFullYear();  // Año actual por defecto
    gastosPendientes: any[] = [];  // Inicializado como un arreglo vacío

    constructor(private apiService: ApiService) {}

    listarGastosPendientes(): void {
      const parametros = {
        mes: this.mes,
        anio: this.anio
      };

      this.apiService.listarGastosPendientes(parametros).subscribe({
        next: (response) => {
          if (response.gastos_pendientes) {
            this.gastosPendientes = response.gastos_pendientes;
          } else {
            this.gastosPendientes = [];  // Asegura que sea un arreglo vacío si no hay datos
          }
        },
        error: (err) => {
          console.error('Error al obtener los gastos pendientes:', err);
          this.gastosPendientes = [];  // En caso de error, asignar un arreglo vacío
        }
      });
    }
  } 

