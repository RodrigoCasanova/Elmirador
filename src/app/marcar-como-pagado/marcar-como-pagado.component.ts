import { Component } from '@angular/core';
import { ApiService } from '../api.service';  // Asegúrate de importar tu servicio API
import { Router } from '@angular/router';
import { FormsModule } from '@angular/forms';  // Para ngModel
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-marcar-como-pagado',
  imports: [CommonModule, FormsModule, RouterModule],
  templateUrl: './marcar-como-pagado.component.html',
  styleUrls: ['./marcar-como-pagado.component.scss']
})
export class MarcarComoPagadoComponent {

  // Variables del formulario
  CodDepto: string = '';
  mes: number = 1;
  anio: number = 2024;
  fecha_pago: string = new Date().toISOString().split('T')[0];  // Establece la fecha actual

  // Mensajes de error o éxito
  mensaje: string = '';
  error: string = '';

  maxFecha: string = new Date().toISOString().split('T')[0];  // Establece la fecha máxima como hoy

  constructor(private apiService: ApiService, private router: Router) {}

  // Método para enviar la solicitud al backend
  marcarComoPagado() {
    // Lógica para marcar el gasto común como pagado
    if (this.CodDepto && this.mes && this.anio) {
      this.mensaje = 'Gasto común marcado como pagado correctamente.';
      this.error = '';
    } else {
      this.error = 'Por favor, complete todos los campos.';
      this.mensaje = '';
    }
  }
}
