let canvasWidth = -1;
let canvasHeight = -1;
let G = 9.806;

export class ProjectileDrawer {
    constructor(canvas, initialValues, landingPosition) {
        this.ctx = canvas.current.getContext("2d");
        this.initialValues = initialValues;
        this.landingPosition = landingPosition;
        if(canvasWidth === -1 || canvasHeight === -1)
        {
            this.getCanvasSize();
        }
        this.setCanvasSize()
    }

    toRadians (angle) {
        return angle * (Math.PI / 180);
    }

    getCanvasSize() {
        const canvasContainer = document.getElementsByClassName("canvas-container")[0];
        canvasWidth = canvasContainer.clientWidth;
        canvasHeight = canvasContainer.clientHeight;
    }

    setCanvasSize() {
        this.ctx.canvas.width = canvasWidth;
        this.ctx.canvas.height = canvasHeight;
        this.startX = 0.03 * canvasWidth;
        this.endX = this.startX + (0.945 * canvasWidth)
        this.startY = 0.03 * canvasHeight
        this.endY = this.startY + (0.9 * canvasHeight)
    }


    drawPoint(x, y, radius = 3) {
        this.ctx.beginPath();
        this.ctx.arc(x, y, radius, 0, Math.PI * 2);
        this.ctx.closePath();
        this.ctx.fill();
    }

    drawYAxis()
    {
        this.ctx.fillStyle = "blue";
        this.ctx.fillRect(this.startX, this.endY, 3, this.startY - this.endY)
    }

    drawXAxis()
    {
        this.ctx.fillStyle = "green";
        this.ctx.fillRect(this.startX , this.endY - 2, this.endX - this.startX, 3)
    }

    drawOriginText(text)
    {
        let oldFillStyle = this.ctx.fillStyle;
        this.ctx.fillStyle = "green";
        this.ctx.font = "1rem Arial";
        this.ctx.fillText(text, this.startX - 20, this.endY + 20)
        this.ctx.fillStyle = oldFillStyle;
    }

    draw()
    {
        this.ctx.strokeStyle = "#ff3636";
        this.ctx.fillStyle = "white";
        this.ctx.fillRect(this.startX, this.startY, this.endX - this.startX, this.endY - this.startY);
        this.drawYAxis()
        this.drawXAxis()
        this.drawPoint(this.startX, this.endY, 4);
        this.ctx.fillStyle = "red";

        let velocity_magnitude = this.initialValues.initialVelocity;
        let angle = this.toRadians(this.initialValues.initialAngle);
        let velocity = {
            x: velocity_magnitude * Math.cos(angle),
            y: velocity_magnitude * Math.sin(angle)
        }
        let point = {
            x: this.startX,
            y: this.endY - this.initialValues.initialHeight
        }

        let originText = "(0, 0)";
        if(point.y < this.startY)
        {
            originText = `(0, ${this.initialValues.initialHeight})`;
            point.y = this.endY;
        }
        this.drawOriginText(originText);

        let yMax = (velocity.y * velocity.y) / (2 * G);
        let time = 2 * velocity.y / G;
        let ratioX = canvasWidth / this.landingPosition;
        let ratioY = canvasHeight / yMax;
        let scaleFactorX = ratioX < 1 ? ratioX : 1;
        let scaleFactorY = ratioY < 1 ? ratioY : 1;
        let timeFactor = 10;
        for (let i = 0; i < time * timeFactor; i++) {
            if(point.x <= this.endX && point.y <= this.endY){
                this.drawPoint(point.x, point.y);

                velocity.y -= G * i / timeFactor;
                point.x += velocity.x * scaleFactorX;
                point.y -= velocity.y * scaleFactorY;

            }
        }

        this.ctx.font = "1rem Arial";
        this.ctx.fillText(`(${parseFloat(this.landingPosition).toFixed(2)}, 0)`, point.x - 30, point.y)
    }
}
