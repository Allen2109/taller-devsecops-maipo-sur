# Laboratorio no desplegable: sin providers, sin recursos.
variable "red_operacional_aprobada" {
  description = "Rango TEST-NET-1 reservado para documentacion; NO es red operativa"
  type        = string
  default     = "192.0.2.0/24"
}
