# https://leetcode.com/problems/event-emitter/

type Callback = (...args: any[]) => any;
type Subscription = {
    unsubscribe: () => void
}

class EventEmitter {
    
    map = new Map<string, Callback[]>();

    subscribe(eventName: string, callback: Callback): Subscription {
        if (!this.map.has(eventName)) {
            this.map.set(eventName, []);
        }

        const arr = this.map.get(eventName);
        arr.push(callback);

        return { unsubscribe: () => arr.splice(arr.indexOf(callback), 1) };
    }

    emit(eventName: string, args: any[] = []): any[] {
        return this.map.get(eventName)?.map(o => o(...args)) ?? [];
    }
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */
