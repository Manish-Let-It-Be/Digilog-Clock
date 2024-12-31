export class DigilogClock {
  constructor(canvas) {
    this.canvas = canvas;
    this.ctx = canvas.getContext('2d');
    this.setCanvasSize();
    window.addEventListener('resize', () => this.setCanvasSize());
    this.update();
  }

  setCanvasSize() {
    const size = Math.min(window.innerWidth * 0.8, 400);
    this.canvas.width = size;
    this.canvas.height = size;
    this.center = size / 2;
    this.radius = (size / 2) * 0.9;
  }

  drawHand(angle, length, text, fontSize, color = 'black') {
    const ctx = this.ctx;
    const angleRad = (angle - 90) * Math.PI / 180;
    const gap = this.radius * 0.02;
    const digits = 5;

    ctx.save();
    ctx.font = `${fontSize}px Arial`;
    ctx.fillStyle = color;
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';

    for (let i = 0; i < digits; i++) {
      const x = this.center + ((length / digits) * (i + 1.5) + gap * i) * Math.cos(angleRad);
      const y = this.center + ((length / digits) * (i + 1.5) + gap * i) * Math.sin(angleRad);
      ctx.fillText(text.trim(), x, y);
    }
    ctx.restore();
  }

  drawClock() {
    const ctx = this.ctx;
    const center = this.center;
    const radius = this.radius;

    ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

    this.drawClockFace(ctx, center, radius);
    this.drawHourMarks(ctx, center, radius);
    this.drawTimeHands(ctx, center, radius);
    this.drawCenterDot(ctx, center);
  }

  drawClockFace(ctx, center, radius) {
    ctx.beginPath();
    ctx.arc(center, center, radius, 0, 2 * Math.PI);
    ctx.strokeStyle = 'black';
    ctx.lineWidth = 2;
    ctx.stroke();
  }

  drawHourMarks(ctx, center, radius) {
    for (let i = 0; i < 12; i++) {
      const angle = (i * 30 - 90) * Math.PI / 180;
      const innerRadius = radius * 0.85;
      const outerRadius = radius * 0.95;
      
      ctx.beginPath();
      ctx.moveTo(
        center + innerRadius * Math.cos(angle),
        center + innerRadius * Math.sin(angle)
      );
      ctx.lineTo(
        center + outerRadius * Math.cos(angle),
        center + outerRadius * Math.sin(angle)
      );
      ctx.strokeStyle = 'black';
      ctx.lineWidth = 2;
      ctx.stroke();
    }
  }

  drawTimeHands(ctx, center, radius) {
    const now = new Date();
    const hours = now.getHours() % 12;
    const minutes = now.getMinutes();
    const seconds = now.getSeconds();

    const hourAngle = (360 / 12) * (hours + minutes / 60);
    const minuteAngle = (360 / 60) * (minutes + seconds / 60);
    const secondAngle = (360 / 60) * seconds;

    this.drawHand(secondAngle, radius * 0.7, `${seconds}`, radius * 0.05, 'red');
    this.drawHand(minuteAngle, radius * 0.6, `${minutes}`, radius * 0.07);
    this.drawHand(hourAngle, radius * 0.5, `${hours}`, radius * 0.09);
  }

  drawCenterDot(ctx, center) {
    ctx.beginPath();
    ctx.arc(center, center, 5, 0, 2 * Math.PI);
    ctx.fillStyle = 'black';
    ctx.fill();
  }

  update() {
    this.drawClock();
    requestAnimationFrame(() => this.update());
  }
}