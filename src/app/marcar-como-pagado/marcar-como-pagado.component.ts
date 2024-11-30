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
  fecha_pago: string = '';

  // Mensajes de error o éxito
  mensaje: string = '';
  error: string = '';

  constructor(private apiService: ApiService, private router: Router) {}

  // Método para enviar la solicitud al backend
  marcarComoPagado() {
    const pagoData = {
      CodDepto: this.CodDepto,
      mes: this.mes,
      anio: this.anio,
      fecha_pago: this.fecha_pago
    };

    this.apiService.marcarComoPagado(pagoData).subscribe(
      (response) => {
        this.mensaje = response.mensaje;
        this.error = ''; // Limpiar el error en caso de éxito
      },
      (err) => {
        this.error = err.error.error || 'Pago duplicado';
        this.mensaje = ''; // Limpiar el mensaje en caso de error
      }
    );
  }
}
